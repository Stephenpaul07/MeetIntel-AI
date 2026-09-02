from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.ai_assistant.serializers import AskQuestionSerializer
from apps.ai_assistant.services.rag import ask_question
from apps.projects.selectors.project import get_project_by_id


class AskQuestionAPIView(APIView):

    def post(self, request, project_id):
        # 1. Check whether the project exists
        project = get_project_by_id(project_id)

        if project is None:
            return Response(
                {"detail": "Project not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # 2. Validate the question
        serializer = AskQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data["question"]

        # 3. Run the complete RAG pipeline
        result = ask_question(
            project_id=project.id,
            question=question,
        )

        # 4. Return the answer
        return Response(
            {
                "question": question,
                "answer": result["answer"],
                "sources": result["sources"],
            },
            status=status.HTTP_200_OK,
        )