from apps.meetings.models import MeetingNote
from apps.projects.models import Project
from apps.ai_assistant.services.indexing import index_meeting_note
from apps.ai_assistant.services.indexing import index_meeting_note
from apps.ai_assistant.services.vector_store import delete_note_chunks
def create_meeting_note(
    *,
    project: Project,
    title: str,
    content: str,
    meeting_date,
) -> MeetingNote:
    meeting_note = MeetingNote.objects.create(
        project=project,
        title=title,
        content=content,
        meeting_date=meeting_date,
    )

    index_meeting_note(meeting_note=meeting_note)

    return meeting_note


def update_meeting_note(
    *,
    meeting_note: MeetingNote,
    title: str,
    content: str,
    meeting_date,
) -> MeetingNote:
    meeting_note.title = title
    meeting_note.content = content
    meeting_note.meeting_date = meeting_date
    meeting_note.save()

    # Keep ChromaDB synchronized
    index_meeting_note(meeting_note=meeting_note)

    return meeting_note

def delete_meeting_note(*, meeting_note: MeetingNote) -> None:
    # Remove vectors first
    delete_note_chunks(
        project_id=meeting_note.project_id,
        meeting_note_id=meeting_note.id,
    )

    # Then remove from SQLite
    meeting_note.delete()