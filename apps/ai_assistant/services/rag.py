from apps.ai_assistant.services.embeddings import generate_embedding
from apps.ai_assistant.services.ollama import generate_answer
from apps.ai_assistant.services.vector_store import search_chunks
from apps.meetings.models import MeetingNote


def ask_question(
    *,
    project_id: int,
    question: str,
) -> dict:
    """
    Complete RAG pipeline:
    Question → Embedding → Vector Search → Context → Ollama → Answer
    """

    # 1. Convert the question into an embedding
    query_embedding = generate_embedding(question)

    # 2. Search for relevant meeting-note chunks
    results = search_chunks(
        project_id=project_id,
        query_embedding=query_embedding,
        n_results=3,
    )

    # 3. Extract retrieved documents
    documents = results.get("documents", [[]])[0]

    # 4. Extract metadata
    metadatas = results.get("metadatas", [[]])[0]

    # If no relevant context exists
    if not documents:
        return {
            "answer": (
                "I could not find relevant information "
                "in the meeting notes."
            ),
            "sources": [],
        }

    # 5. Combine retrieved chunks into context
    context = "\n\n".join(documents)

    # 6. Generate answer using Ollama
    answer = generate_answer(
        question=question,
        context=context,
    )

    # 7. Prepare enriched source information
    sources = []

    seen_sources = set()

    for document, metadata in zip(documents, metadatas):

        meeting_note_id = metadata.get("meeting_note_id")
        chunk_index = metadata.get("chunk_index")

        # Avoid duplicate sources
        source_key = (
            meeting_note_id,
            chunk_index,
        )

        if source_key in seen_sources:
            continue

        seen_sources.add(source_key)

        # Get the original meeting note
        try:

            meeting_note = MeetingNote.objects.get(
                id=meeting_note_id,
                project_id=project_id,
            )

            source = {
                "meeting_note_id": meeting_note.id,
                "meeting_note_title": meeting_note.title,
                "meeting_date": (
                    meeting_note.meeting_date.isoformat()
                    if meeting_note.meeting_date
                    else None
                ),
                "chunk_index": chunk_index,
                "relevant_text": document,
            }

        except MeetingNote.DoesNotExist:

            # Fallback if note was deleted
            source = {
                "meeting_note_id": meeting_note_id,
                "meeting_note_title": "Meeting Note",
                "meeting_date": None,
                "chunk_index": chunk_index,
                "relevant_text": document,
            }

        sources.append(source)

    return {
        "answer": answer,
        "sources": sources,
    }