from apps.projects.models import Project


def create_project(*, name: str, description: str = "") -> Project:
    project = Project.objects.create(
        name=name,
        description=description,
    )
    return project


def update_project(*, project: Project, name: str, description: str = "") -> Project:
    project.name = name
    project.description = description
    project.save()

    return project


def delete_project(*, project: Project) -> None:
    project.delete()