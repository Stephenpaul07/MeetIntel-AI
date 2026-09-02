from apps.meetings.models import MeetingNote


def get_meeting_notes_by_project(*, project_id: int):
    return (
        MeetingNote.objects
        .filter(project_id=project_id)
        .order_by("-meeting_date", "-created_at")
    )


def get_meeting_note_by_id(*, meeting_note_id: int):
    return (
        MeetingNote.objects
        .filter(id=meeting_note_id)
        .first()
    )