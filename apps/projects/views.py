from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.projects.models import Project
from apps.projects.selectors.project import (
    get_all_projects,
    get_project_by_id,
)
from apps.projects.serializers import ProjectSerializer
from apps.projects.services.project import (
    create_project,
    update_project,
    delete_project,
)


class ProjectViewSet(viewsets.ViewSet):

    def list(self, request):
        projects = get_all_projects()
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = get_project_by_id(pk)

        if project is None:
            return Response(
                {"detail": "Project not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = create_project(
            name=serializer.validated_data["name"],
            description=serializer.validated_data.get("description", ""),
        )

        response_serializer = ProjectSerializer(project)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, pk=None):
        project = get_project_by_id(pk)

        if project is None:
            return Response(
                {"detail": "Project not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ProjectSerializer(
            project,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)

        project = update_project(
            project=project,
            name=serializer.validated_data["name"],
            description=serializer.validated_data.get("description", ""),
        )

        return Response(ProjectSerializer(project).data)

    def partial_update(self, request, pk=None):
        project = get_project_by_id(pk)

        if project is None:
            return Response(
                {"detail": "Project not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ProjectSerializer(
            project,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        project = update_project(
            project=project,
            name=serializer.validated_data.get("name", project.name),
            description=serializer.validated_data.get(
                "description",
                project.description,
            ),
        )

        return Response(ProjectSerializer(project).data)

    def destroy(self, request, pk=None):
        project = get_project_by_id(pk)

        if project is None:
            return Response(
                {"detail": "Project not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        delete_project(project=project)

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

from django.shortcuts import render


def dashboard_view(request):
    return render(request, "dashboard.html")