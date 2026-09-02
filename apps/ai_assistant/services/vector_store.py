import chromadb


_client = chromadb.PersistentClient(
    path="chroma_db"
)


def get_project_collection(project_id: int):
    return _client.get_or_create_collection(
        name=f"project_{project_id}"
    )


def add_chunks(
    *,
    project_id: int,
    meeting_note_id: int,
    chunks: list[str],
    embeddings: list[list[float]],
):
    collection = get_project_collection(project_id)

    ids = [
        f"note_{meeting_note_id}_chunk_{index}"
        for index in range(len(chunks))
    ]

    metadatas = [
        {
            "project_id": project_id,
            "meeting_note_id": meeting_note_id,
            "chunk_index": index,
        }
        for index in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search_chunks(
    *,
    project_id: int,
    query_embedding: list[float],
    n_results: int = 3,
):
    collection = get_project_collection(project_id)

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )

def delete_note_chunks(
    *,
    project_id: int,
    meeting_note_id: int,
):
    collection = get_project_collection(project_id)

    collection.delete(
        where={
            "meeting_note_id": meeting_note_id
        }
    )