from django.urls import path

from apps.meetings.views import MeetingNoteViewSet


meeting_note_list = MeetingNoteViewSet.as_view({
    "get": "list",
    "post": "create",
})

meeting_note_detail = MeetingNoteViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})


urlpatterns = [
    path(
        "projects/<int:project_id>/notes/",
        meeting_note_list,
        name="meeting-note-list",
    ),
    path(
        "notes/<int:pk>/",
        meeting_note_detail,
        name="meeting-note-detail",
    ),
]