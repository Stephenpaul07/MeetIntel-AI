from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.meetings.selectors.meeting_note import (
    get_meeting_note_by_id,
    get_meeting_notes_by_project,
)
from apps.meetings.serializers import MeetingNoteSerializer
from apps.meetings.services.meeting_note import (
    create_meeting_note,
    delete_meeting_note,
    update_meeting_note,
)
from apps.projects.selectors.project import get_project_by_id


class MeetingNoteViewSet(viewsets.ViewSet):

    def list(self, request, project_id=None):
        project = get_project_by_id(project_id)

        if project is None:
            return Response(
                {"detail": "Project not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        meeting_notes = get_meeting_notes_by_project(
            project_id=project.id
        )

        serializer = MeetingNoteSerializer(
            meeting_notes,
            many=True,
        )

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        meeting_note = get_meeting_note_by_id(
            meeting_note_id=pk
        )

        if meeting_note is None:
            return Response(
                {"detail": "Meeting note not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MeetingNoteSerializer(meeting_note)

        return Response(serializer.data)

    def create(self, request, project_id=None):
        project = get_project_by_id(project_id)

        if project is None:
            return Response(
                {"detail": "Project not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MeetingNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        meeting_note = create_meeting_note(
            project=project,
            title=serializer.validated_data["title"],
            content=serializer.validated_data["content"],
            meeting_date=serializer.validated_data["meeting_date"],
        )

        return Response(
            MeetingNoteSerializer(meeting_note).data,
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):
        meeting_note = get_meeting_note_by_id(
            meeting_note_id=pk
        )

        if meeting_note is None:
            return Response(
                {"detail": "Meeting note not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MeetingNoteSerializer(
            meeting_note,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)

        meeting_note = update_meeting_note(
            meeting_note=meeting_note,
            title=serializer.validated_data["title"],
            content=serializer.validated_data["content"],
            meeting_date=serializer.validated_data["meeting_date"],
        )

        return Response(MeetingNoteSerializer(meeting_note).data)

    def partial_update(self, request, pk=None):
        meeting_note = get_meeting_note_by_id(
            meeting_note_id=pk
        )

        if meeting_note is None:
            return Response(
                {"detail": "Meeting note not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = MeetingNoteSerializer(
            meeting_note,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        meeting_note = update_meeting_note(
            meeting_note=meeting_note,
            title=serializer.validated_data.get(
                "title",
                meeting_note.title,
            ),
            content=serializer.validated_data.get(
                "content",
                meeting_note.content,
            ),
            meeting_date=serializer.validated_data.get(
                "meeting_date",
                meeting_note.meeting_date,
            ),
        )

        return Response(MeetingNoteSerializer(meeting_note).data)

    def destroy(self, request, pk=None):
        meeting_note = get_meeting_note_by_id(
            meeting_note_id=pk
        )

        if meeting_note is None:
            return Response(
                {"detail": "Meeting note not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        delete_meeting_note(meeting_note=meeting_note)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )