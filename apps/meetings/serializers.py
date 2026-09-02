from rest_framework import serializers

from apps.meetings.models import MeetingNote


class MeetingNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingNote
        fields = [
            "id",
            "project",
            "title",
            "content",
            "meeting_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "project",
            "created_at",
            "updated_at",
        ]