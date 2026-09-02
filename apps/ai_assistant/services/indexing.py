from apps.ai_assistant.services.chunking import chunk_text
from apps.ai_assistant.services.embeddings import generate_embeddings
from apps.ai_assistant.services.vector_store import (
    add_chunks,
    delete_note_chunks,
)
from apps.meetings.models import MeetingNote


def index_meeting_note(*, meeting_note: MeetingNote) -> None:
    """
    Re-index a meeting note in ChromaDB.
    """

    delete_note_chunks(
        project_id=meeting_note.project_id,
        meeting_note_id=meeting_note.id,
    )

    chunks = chunk_text(meeting_note.content)

    if not chunks:
        return

    embeddings = generate_embeddings(chunks)

    add_chunks(
        project_id=meeting_note.project_id,
        meeting_note_id=meeting_note.id,
        chunks=chunks,
        embeddings=embeddings,
    )