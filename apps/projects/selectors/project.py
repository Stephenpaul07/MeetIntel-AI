from apps.projects.models import Project


def get_all_projects():
    return Project.objects.all().order_by("-created_at")


def get_project_by_id(project_id):
    return Project.objects.filter(id=project_id).first()