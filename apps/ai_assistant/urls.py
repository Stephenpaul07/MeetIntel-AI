from django.urls import path

from apps.ai_assistant.views import AskQuestionAPIView


urlpatterns = [
    path(
        "projects/<int:project_id>/ask/",
        AskQuestionAPIView.as_view(),
        name="ask-question",
    ),
]