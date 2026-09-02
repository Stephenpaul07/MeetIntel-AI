from django.db import models

from apps.projects.models import Project


class MeetingNote(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="meeting_notes",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    meeting_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title