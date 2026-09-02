import requests

from nicegui import ui, run


API_BASE_URL = "http://127.0.0.1:8000/api"


# ============================================================
# GLOBAL STYLE
# ============================================================

ui.add_head_html(
    """
    <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600&display=swap'
        );

        :root {
            --white: #F7F7F2;
            --black: #111111;
        }

        * {
            box-sizing: border-box;
        }

        html,
        body {
            margin: 0;
            padding: 0;
            background: var(--white);
            color: var(--black);
            font-family: 'DM Sans', sans-serif;
        }

        .q-page-container,
        .q-page {
            background: var(--white);
        }

        .premium-app {
            min-height: 100vh;
            background: var(--white);
        }

        /* ------------------------------------------------
           SIDEBAR
        ------------------------------------------------ */

        .sidebar {
            width: 250px;
            min-height: 100vh;
            background: var(--white);
            border-right: 1px solid var(--black);
            position: fixed;
            top: 0;
            left: 0;
            z-index: 100;
        }

        .sidebar-top {
            padding: 28px 24px;
        }

        .sidebar-bottom {
            padding: 24px;
        }

        .main-area {
            margin-left: 250px;
            min-height: 100vh;
            background: var(--white);
        }

        .page-content {
            width: 100%;
            max-width: 1500px;
            margin: 0 auto;
            padding: 56px 72px 100px 72px;
        }

        /* ------------------------------------------------
           BRAND
        ------------------------------------------------ */

        .brand-mark {
            width: 36px;
            height: 36px;
            background: var(--black);
            color: var(--white);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: -1px;
        }

        .brand-title {
            color: var(--black);
            font-size: 17px;
            font-weight: 700;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }

        .brand-subtitle {
            color: var(--black);
            opacity: 0.55;
            font-size: 10px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        /* ------------------------------------------------
           NAVIGATION
        ------------------------------------------------ */

        .nav-section-title {
            color: var(--black);
            opacity: 0.45;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 0 10px;
        }

        .nav-item {
            width: 100%;
            min-height: 44px;
            padding: 0 12px;
            color: var(--black);
            opacity: 0.58;
            border-radius: 0;
            transition: all 0.2s ease;
            cursor: pointer;
        }

        .nav-item:hover {
            opacity: 1;
            background: var(--black);
            color: var(--white);
        }

        .nav-item-active {
            opacity: 1;
            background: var(--black);
            color: var(--white);
        }

        .sidebar-divider {
            height: 1px;
            width: 100%;
            background: var(--black);
            opacity: 0.15;
        }

        /* ------------------------------------------------
           PAGE HEADER
        ------------------------------------------------ */

        .page-eyebrow {
            color: var(--black);
            opacity: 0.5;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .page-title {
            color: var(--black);
            font-family: 'Playfair Display', serif;
            font-size: 56px;
            font-weight: 500;
            line-height: 1;
            letter-spacing: -2px;
        }

        .project-page-title {
            color: var(--black);
            font-family: 'Playfair Display', serif;
            font-size: 48px;
            font-weight: 500;
            line-height: 1.1;
            letter-spacing: -1.5px;
        }

        .page-subtitle {
            max-width: 620px;
            color: var(--black);
            opacity: 0.62;
            font-size: 15px;
            line-height: 1.8;
        }

        .section-heading {
            color: var(--black);
            font-size: 22px;
            font-weight: 600;
            letter-spacing: -0.6px;
        }

        .section-label {
            color: var(--black);
            opacity: 0.5;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }

        .meta-text {
            color: var(--black);
            opacity: 0.45;
            font-size: 11px;
            line-height: 1.5;
        }

        .premium-divider {
            width: 100%;
            height: 1px;
            background: var(--black);
            opacity: 0.15;
        }

        /* ------------------------------------------------
           BUTTONS
        ------------------------------------------------ */

        .premium-button {
            background: var(--black) !important;
            color: var(--white) !important;
            border: 1px solid var(--black) !important;
            border-radius: 0 !important;
            min-height: 46px !important;
            padding: 0 20px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            letter-spacing: 0 !important;
            box-shadow: none !important;
            transition: all 0.2s ease !important;
        }

        .premium-button:hover {
            background: var(--white) !important;
            color: var(--black) !important;
        }

        .secondary-button {
            background: var(--white) !important;
            color: var(--black) !important;
            border: 1px solid var(--black) !important;
            border-radius: 0 !important;
            min-height: 44px !important;
            padding: 0 18px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            box-shadow: none !important;
            transition: all 0.2s ease !important;
        }

        .secondary-button:hover {
            background: var(--black) !important;
            color: var(--white) !important;
        }

        .icon-button {
            color: var(--black) !important;
            border: 1px solid var(--black) !important;
            border-radius: 50% !important;
            background: var(--white) !important;
        }

        .icon-button:hover {
            background: var(--black) !important;
            color: var(--white) !important;
        }

        /* ------------------------------------------------
           PROJECT GRID
        ------------------------------------------------ */

        .project-grid {
            width: 100%;
            display: grid;
            grid-template-columns:
                repeat(auto-fill, minmax(300px, 1fr));
            gap: 1px;
            background: var(--black);
            border: 1px solid var(--black);
        }

        .project-card {
            min-height: 260px;
            padding: 30px;
            background: var(--white);
            border-radius: 0;
            box-shadow: none;
            cursor: pointer;
            transition:
                background 0.25s ease,
                color 0.25s ease;
        }

        .project-card:hover {
            background: var(--black);
            color: var(--white);
        }

        .project-card:hover .project-name,
        .project-card:hover .project-description,
        .project-card:hover .project-meta,
        .project-card:hover .project-arrow {
            color: var(--white) !important;
            opacity: 1 !important;
        }

        .project-number {
            color: var(--black);
            opacity: 0.35;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
        }

        .project-card:hover .project-number {
            color: var(--white);
            opacity: 0.6;
        }

        .project-name {
            color: var(--black);
            font-size: 20px;
            font-weight: 600;
            letter-spacing: -0.5px;
            transition: color 0.25s ease;
        }

        .project-description {
            color: var(--black);
            opacity: 0.58;
            font-size: 13px;
            line-height: 1.75;
            transition: color 0.25s ease;
        }

        .project-meta {
            color: var(--black);
            opacity: 0.4;
            font-size: 11px;
        }

        .project-arrow {
            color: var(--black);
            opacity: 0.5;
            transition: color 0.25s ease;
        }

        /* ------------------------------------------------
           EMPTY STATE
        ------------------------------------------------ */

        .empty-state {
            width: 100%;
            min-height: 300px;
            padding: 60px 30px;
            border: 1px solid var(--black);
            background: var(--white);
            text-align: center;
        }

        .empty-mark {
            width: 44px;
            height: 44px;
            background: var(--black);
            color: var(--white);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 22px;
        }

        /* ------------------------------------------------
           DIALOG
        ------------------------------------------------ */

        .dialog-card {
            width: 520px;
            max-width: 94vw;
            padding: 34px;
            background: var(--white) !important;
            border: 1px solid var(--black);
            border-radius: 0 !important;
            box-shadow: 12px 12px 0 var(--black);
        }

        .dialog-title {
            color: var(--black);
            font-family: 'Playfair Display', serif;
            font-size: 30px;
            font-weight: 500;
            letter-spacing: -0.8px;
        }

        /* ------------------------------------------------
           INPUTS
        ------------------------------------------------ */

        .premium-input .q-field__control,
        .ask-input .q-field__control {
            border-radius: 0 !important;
            background: var(--white) !important;
        }

        .premium-input.q-field--outlined .q-field__control:before,
        .ask-input.q-field--outlined .q-field__control:before {
            border-color: var(--black) !important;
            opacity: 0.3;
        }

        .premium-input.q-field--outlined.q-field--focused .q-field__control:after,
        .ask-input.q-field--outlined.q-field--focused .q-field__control:after {
            border-color: var(--black) !important;
        }

        .premium-input .q-field__label,
        .ask-input .q-field__label {
            color: var(--black) !important;
            opacity: 0.5;
        }

        .premium-input input,
        .premium-input textarea,
        .ask-input input {
            color: var(--black) !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        /* ------------------------------------------------
           TABS
        ------------------------------------------------ */

        .q-tabs {
            border-bottom: 1px solid rgba(17, 17, 17, 0.15);
        }

        .q-tab {
            min-height: 52px;
            color: var(--black) !important;
            opacity: 0.45;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 0.2px;
        }

        .q-tab--active {
            opacity: 1 !important;
        }

        .q-tab__indicator {
            background: var(--black) !important;
            height: 2px !important;
        }

        /* ------------------------------------------------
           NOTES
        ------------------------------------------------ */

        .note-card {
            width: 100%;
            padding: 26px 0;
            background: transparent;
            border-radius: 0;
            border: none;
            border-bottom: 1px solid rgba(17, 17, 17, 0.15);
            box-shadow: none;
        }

        .note-title {
            color: var(--black);
            font-family: 'Playfair Display', serif;
            font-size: 22px;
            font-weight: 500;
            letter-spacing: -0.5px;
        }

        .note-preview {
            color: var(--black);
            opacity: 0.62;
            font-size: 14px;
            line-height: 1.8;
            max-width: 900px;
        }

        .delete-button {
            color: var(--black) !important;
            opacity: 0.45;
        }

        .delete-button:hover {
            opacity: 1;
            background: transparent !important;
        }

        .q-expansion-item {
            border: none !important;
        }

        .q-expansion-item__toggle-icon {
            color: var(--black) !important;
        }

        /* ------------------------------------------------
           AI WORKSPACE
        ------------------------------------------------ */

        .ai-shell {
            width: 100%;
            min-height: 650px;
            border: 1px solid var(--black);
            background: var(--white);
            display: flex;
            flex-direction: column;
        }

        .chat-scroll {
            height: 540px;
            overflow-y: auto;
            padding: 44px;
            background: var(--white);
        }

        .chat-scroll::-webkit-scrollbar {
            width: 4px;
        }

        .chat-scroll::-webkit-scrollbar-thumb {
            background: var(--black);
        }

        .welcome-mark,
        .ai-avatar {
            width: 34px;
            height: 34px;
            background: var(--black);
            color: var(--white);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .ai-name {
            color: var(--black);
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.2px;
        }

        .ai-response {
            max-width: 900px;
        }

        .ai-answer {
            color: var(--black);
            font-size: 15px;
            line-height: 1.9;
            white-space: pre-wrap;
            padding-left: 46px;
        }

        .user-question {
            max-width: 72%;
            margin-left: auto;
            padding: 16px 20px;
            background: var(--black);
            color: var(--white);
            font-size: 14px;
            line-height: 1.7;
        }

        .source-box {
            margin-left: 46px;
            margin-top: 16px;
            padding: 18px;
            border-top: 1px solid var(--black);
            border-bottom: 1px solid var(--black);
        }

        .source-title {
            color: var(--black);
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 4px;
        }

        .source-item {
            color: var(--black);
            opacity: 0.6;
            font-size: 12px;
            line-height: 1.6;
        }

        .ai-input-area {
            padding: 20px 22px;
            border-top: 1px solid var(--black);
            background: var(--white);
        }

        .ask-input .q-field__control {
            min-height: 54px !important;
        }

        .send-button {
            min-width: 48px !important;
            width: 48px !important;
            height: 48px !important;
            padding: 0 !important;
            border-radius: 50% !important;
            background: var(--black) !important;
            color: var(--white) !important;
            border: 1px solid var(--black) !important;
        }

        .send-button:hover {
            background: var(--white) !important;
            color: var(--black) !important;
        }

        .loading-text {
            color: var(--black);
            opacity: 0.55;
            font-size: 12px;
            font-style: italic;
        }

        /* ------------------------------------------------
           RESPONSIVE
        ------------------------------------------------ */

        @media (max-width: 900px) {

            .sidebar {
                display: none;
            }

            .main-area {
                margin-left: 0;
            }

            .page-content {
                padding: 36px 22px 70px 22px;
            }

            .page-title {
                font-size: 42px;
            }

            .project-page-title {
                font-size: 38px;
            }

            .chat-scroll {
                height: 500px;
                padding: 24px;
            }

            .ai-answer,
            .source-box {
                margin-left: 0;
                padding-left: 0;
            }

            .user-question {
                max-width: 90%;
            }

            .project-grid {
                grid-template-columns: 1fr;
            }

        }

    </style>
    """,
    shared=True,
)


# ============================================================
# API FUNCTIONS
# ============================================================

def api_get(url, timeout=10):

    response = requests.get(
        url,
        timeout=timeout,
    )

    response.raise_for_status()

    return response.json()


def api_post(url, data, timeout=30):

    response = requests.post(
        url,
        json=data,
        timeout=timeout,
    )

    response.raise_for_status()

    return response.json()


def get_projects():

    return api_get(
        f"{API_BASE_URL}/projects/"
    )


def get_project(project_id):

    return api_get(
        f"{API_BASE_URL}/projects/{project_id}/"
    )


def create_project(name, description):

    return api_post(
        f"{API_BASE_URL}/projects/",
        {
            "name": name,
            "description": description,
        },
    )


def get_notes(project_id):

    return api_get(
        f"{API_BASE_URL}/projects/{project_id}/notes/"
    )


def create_note(
    project_id,
    title,
    content,
    meeting_date,
):

    return api_post(
        f"{API_BASE_URL}/projects/{project_id}/notes/",
        {
            "title": title,
            "content": content,
            "meeting_date": meeting_date,
        },
    )


def delete_note(note_id):

    response = requests.delete(
        f"{API_BASE_URL}/notes/{note_id}/",
        timeout=10,
    )

    response.raise_for_status()


def ask_ai(
    project_id,
    question,
):

    return api_post(
        f"{API_BASE_URL}/projects/{project_id}/ask/",
        {
            "question": question,
        },
        timeout=120,
    )


# ============================================================
# SIDEBAR
# ============================================================

def create_sidebar():

    with ui.column().classes(
        "sidebar justify-between no-wrap"
    ):

        with ui.column().classes(
            "sidebar-top w-full gap-10"
        ):

            with ui.row().classes(
                "items-center gap-3"
            ):

                ui.html(
                    '<div class="brand-mark">M</div>'
                )

                with ui.column().classes(
                    "gap-0"
                ):

                    ui.label(
                        "MeetIntel AI"
                    ).classes(
                        "brand-title"
                    )

                    ui.label(
                        "Meeting Intelligence"
                    ).classes(
                        "brand-subtitle"
                    )

            with ui.column().classes(
                "w-full gap-2"
            ):

                ui.label(
                    "Workspace"
                ).classes(
                    "nav-section-title"
                )

                with ui.row().classes(
                    "nav-item nav-item-active items-center gap-3"
                ).on(
                    "click",
                    lambda: ui.navigate.to("/")
                ):

                    ui.icon(
                        "folder_open",
                        size="18px",
                    )

                    ui.label(
                        "Projects"
                    ).classes(
                        "text-sm"
                    )

        with ui.column().classes(
            "sidebar-bottom w-full gap-4"
        ):

            ui.html(
                '<div class="sidebar-divider"></div>'
            )

            with ui.row().classes(
                "items-center gap-3 pt-2"
            ):

                ui.html(
                    """
                    <div class="welcome-mark">
                        <span class="material-icons" style="font-size:15px">
                            auto_awesome
                        </span>
                    </div>
                    """
                )

                with ui.column().classes(
                    "gap-0"
                ):

                    ui.label(
                        "Private Intelligence"
                    ).classes(
                        "text-xs font-semibold"
                    )

                    ui.label(
                        "Local AI workspace"
                    ).classes(
                        "meta-text"
                    )


# ============================================================
# PROJECT CARD
# ============================================================

def render_project_card(project):

    project_id = project.get("id")

    with ui.card().classes(
        "project-card"
    ).on(
        "click",
        lambda: ui.navigate.to(
            f"/projects/{project_id}"
        ),
    ):

        with ui.row().classes(
            "w-full justify-between items-start"
        ):

            ui.label(
                f"{project_id:02d}"
            ).classes(
                "project-number"
            )

            ui.icon(
                "arrow_outward",
                size="20px",
            ).classes(
                "project-arrow"
            )

        ui.space()

        ui.label(
            project.get(
                "name",
                "Untitled Project",
            )
        ).classes(
            "project-name"
        )

        description = (
            project.get("description")
            or "A private workspace for meeting intelligence."
        )

        ui.label(
            description
        ).classes(
            "project-description mt-2"
        )

        ui.space()

        ui.label(
            "Open workspace"
        ).classes(
            "project-meta"
        )


# ============================================================
# DASHBOARD
# ============================================================

@ui.page("/")
def dashboard():

    create_sidebar()

    with ui.column().classes(
        "main-area premium-app"
    ):

        with ui.column().classes(
            "page-content gap-0"
        ):

            with ui.row().classes(
                "w-full items-start justify-between"
            ):

                with ui.column().classes(
                    "gap-4"
                ):

                    ui.label(
                        "MEETING INTELLIGENCE"
                    ).classes(
                        "page-eyebrow"
                    )

                    ui.label(
                        "Projects"
                    ).classes(
                        "page-title"
                    )

                    ui.label(
                        "A private workspace for your conversations, decisions, and institutional knowledge."
                    ).classes(
                        "page-subtitle"
                    )

                create_button = ui.button(
                    "+ New Project"
                ).classes(
                    "premium-button"
                )

            ui.html(
                '<div class="premium-divider" style="margin:56px 0 28px 0"></div>'
            )

            with ui.row().classes(
                "w-full items-center justify-between mb-6"
            ):

                ui.label(
                    "Your workspace"
                ).classes(
                    "section-label"
                )

                project_count = ui.label(
                    ""
                ).classes(
                    "meta-text"
                )

            projects_container = ui.column().classes(
                "w-full"
            )

            # ------------------------------------------------
            # CREATE PROJECT DIALOG
            # ------------------------------------------------

            with ui.dialog() as project_dialog:

                with ui.card().classes(
                    "dialog-card"
                ):

                    ui.label(
                        "Create a project"
                    ).classes(
                        "dialog-title"
                    )

                    ui.label(
                        "Create a dedicated space for the conversations and intelligence that matter."
                    ).classes(
                        "page-subtitle mt-2 mb-5"
                    )

                    project_name = ui.input(
                        label="Project name"
                    ).classes(
                        "w-full premium-input"
                    )

                    project_description = ui.textarea(
                        label="Description"
                    ).classes(
                        "w-full premium-input"
                    )

                    def submit_project():

                        name = (
                            project_name.value
                            or ""
                        ).strip()

                        description = (
                            project_description.value
                            or ""
                        ).strip()

                        if not name:

                            ui.notify(
                                "Project name is required.",
                                type="warning",
                            )

                            return

                        try:

                            create_project(
                                name,
                                description,
                            )

                            project_dialog.close()

                            project_name.value = ""
                            project_description.value = ""

                            ui.notify(
                                "Project created successfully.",
                                type="positive",
                            )

                            load_projects()

                        except requests.RequestException as error:

                            ui.notify(
                                f"Could not create project: {error}",
                                type="negative",
                            )

                    with ui.row().classes(
                        "w-full justify-end gap-3 mt-4"
                    ):

                        ui.button(
                            "Cancel",
                            on_click=project_dialog.close,
                        ).classes(
                            "secondary-button"
                        )

                        ui.button(
                            "Create Project",
                            on_click=submit_project,
                        ).classes(
                            "premium-button"
                        )

            create_button.on(
                "click",
                project_dialog.open,
            )

            # ------------------------------------------------
            # LOAD PROJECTS
            # ------------------------------------------------

            def load_projects():

                projects_container.clear()

                try:

                    projects = get_projects()

                    if not projects:

                        project_count.text = "0 projects"

                        with projects_container:

                            with ui.column().classes(
                                "empty-state items-center justify-center"
                            ):

                                ui.html(
                                    """
                                    <div class="empty-mark">
                                        <span class="material-icons">
                                            folder_open
                                        </span>
                                    </div>
                                    """
                                )

                                ui.label(
                                    "Your workspace is empty"
                                ).classes(
                                    "section-heading"
                                )

                                ui.label(
                                    "Create your first project and begin building a private intelligence layer around your meetings."
                                ).classes(
                                    "page-subtitle mt-2"
                                )

                                ui.button(
                                    "Create your first project",
                                    on_click=project_dialog.open,
                                ).classes(
                                    "premium-button mt-5"
                                )

                        return

                    project_count.text = (
                        f"{len(projects)} projects"
                    )

                    with projects_container:

                        with ui.element(
                            "div"
                        ).classes(
                            "project-grid"
                        ):

                            for project in projects:

                                render_project_card(
                                    project
                                )

                except requests.RequestException as error:

                    project_count.text = ""

                    with projects_container:

                        with ui.column().classes(
                            "empty-state items-center justify-center"
                        ):

                            ui.label(
                                "Unable to connect"
                            ).classes(
                                "section-heading"
                            )

                            ui.label(
                                "Make sure the Django server is running."
                            ).classes(
                                "page-subtitle mt-2"
                            )

                            ui.label(
                                str(error)
                            ).classes(
                                "meta-text mt-3"
                            )

            load_projects()


# ============================================================
# PROJECT PAGE
# ============================================================

@ui.page("/projects/{project_id}")
def project_page(project_id: int):

    create_sidebar()

    with ui.column().classes(
        "main-area premium-app"
    ):

        with ui.column().classes(
            "page-content gap-0"
        ):

            project = {}

            try:

                project = get_project(
                    project_id
                )

            except requests.RequestException:

                project = {
                    "id": project_id,
                    "name": "Project",
                    "description": "",
                }

            # ------------------------------------------------
            # BACK NAVIGATION
            # ------------------------------------------------

            with ui.row().classes(
                "w-full items-center gap-3 mb-12"
            ):

                ui.button(
                    icon="arrow_back",
                    on_click=lambda: ui.navigate.to("/"),
                ).props(
                    "flat round"
                ).classes(
                    "icon-button"
                )

                ui.label(
                    "All projects"
                ).classes(
                    "meta-text"
                )

            # ------------------------------------------------
            # PROJECT HEADER
            # ------------------------------------------------

            ui.label(
                "PROJECT WORKSPACE"
            ).classes(
                "page-eyebrow"
            )

            ui.label(
                project.get(
                    "name",
                    "Untitled Project",
                )
            ).classes(
                "project-page-title mt-4"
            )

            description = (
                project.get("description")
                or "A private workspace for meetings, context, and intelligence."
            )

            ui.label(
                description
            ).classes(
                "page-subtitle mt-4"
            )

            ui.html(
                '<div class="premium-divider" style="margin:52px 0 0 0"></div>'
            )

            # ------------------------------------------------
            # TABS
            # ------------------------------------------------

            with ui.tabs().classes(
                "w-full"
            ) as tabs:

                notes_tab = ui.tab(
                    "Meeting Notes",
                    icon="description",
                )

                ai_tab = ui.tab(
                    "Ask Intelligence",
                    icon="auto_awesome",
                )

            with ui.tab_panels(
                tabs,
                value=notes_tab,
            ).classes(
                "w-full bg-transparent"
            ):

                # ============================================
                # MEETING NOTES
                # ============================================

                with ui.tab_panel(
                    notes_tab
                ).classes(
                    "p-0 pt-10"
                ):

                    with ui.row().classes(
                        "w-full items-end justify-between mb-10"
                    ):

                        with ui.column().classes(
                            "gap-2"
                        ):

                            ui.label(
                                "Meeting Notes"
                            ).classes(
                                "section-heading"
                            )

                            ui.label(
                                "A living record of your conversations and decisions."
                            ).classes(
                                "page-subtitle"
                            )

                        add_note_button = ui.button(
                            "+ Add Meeting Note"
                        ).classes(
                            "premium-button"
                        )

                    notes_container = ui.column().classes(
                        "w-full"
                    )

                    # ----------------------------------------
                    # ADD NOTE DIALOG
                    # ----------------------------------------

                    with ui.dialog() as note_dialog:

                        with ui.card().classes(
                            "dialog-card"
                        ):

                            ui.label(
                                "Add meeting note"
                            ).classes(
                                "dialog-title"
                            )

                            ui.label(
                                "Capture the important context from a conversation."
                            ).classes(
                                "page-subtitle mt-2 mb-5"
                            )

                            note_title = ui.input(
                                label="Meeting title"
                            ).classes(
                                "w-full premium-input"
                            )

                            note_date = ui.input(
                                label="Meeting date"
                            ).classes(
                                "w-full premium-input"
                            )

                            note_date.props(
                                "type=date"
                            )

                            note_content = ui.textarea(
                                label="Meeting content"
                            ).classes(
                                "w-full premium-input"
                            )

                            note_content.props(
                                "autogrow"
                            )

                            def submit_note():

                                title = (
                                    note_title.value
                                    or ""
                                ).strip()

                                content = (
                                    note_content.value
                                    or ""
                                ).strip()

                                meeting_date = (
                                    note_date.value
                                    or ""
                                )

                                if not title:

                                    ui.notify(
                                        "Meeting title is required.",
                                        type="warning",
                                    )

                                    return

                                if not content:

                                    ui.notify(
                                        "Meeting content is required.",
                                        type="warning",
                                    )

                                    return

                                try:

                                    create_note(
                                        project_id,
                                        title,
                                        content,
                                        meeting_date,
                                    )

                                    note_dialog.close()

                                    note_title.value = ""
                                    note_content.value = ""
                                    note_date.value = ""

                                    ui.notify(
                                        "Meeting note added successfully.",
                                        type="positive",
                                    )

                                    load_notes()

                                except requests.RequestException as error:

                                    ui.notify(
                                        f"Could not add meeting note: {error}",
                                        type="negative",
                                    )

                            with ui.row().classes(
                                "w-full justify-end gap-3 mt-5"
                            ):

                                ui.button(
                                    "Cancel",
                                    on_click=note_dialog.close,
                                ).classes(
                                    "secondary-button"
                                )

                                ui.button(
                                    "Save Note",
                                    on_click=submit_note,
                                ).classes(
                                    "premium-button"
                                )

                    add_note_button.on(
                        "click",
                        note_dialog.open,
                    )

                    # ----------------------------------------
                    # DELETE DIALOG
                    # ----------------------------------------

                    with ui.dialog() as delete_dialog:

                        with ui.card().classes(
                            "dialog-card"
                        ):

                            ui.label(
                                "Delete this note?"
                            ).classes(
                                "dialog-title"
                            )

                            ui.label(
                                "This action cannot be undone."
                            ).classes(
                                "page-subtitle mt-2"
                            )

                            note_id_to_delete = {
                                "value": None
                            }

                            def confirm_delete():

                                note_id = (
                                    note_id_to_delete[
                                        "value"
                                    ]
                                )

                                if note_id is None:
                                    return

                                try:

                                    delete_note(
                                        note_id
                                    )

                                    delete_dialog.close()

                                    ui.notify(
                                        "Meeting note deleted.",
                                        type="positive",
                                    )

                                    load_notes()

                                except requests.RequestException as error:

                                    ui.notify(
                                        f"Could not delete note: {error}",
                                        type="negative",
                                    )

                            with ui.row().classes(
                                "w-full justify-end gap-3 mt-5"
                            ):

                                ui.button(
                                    "Cancel",
                                    on_click=delete_dialog.close,
                                ).classes(
                                    "secondary-button"
                                )

                                ui.button(
                                    "Delete",
                                    on_click=confirm_delete,
                                ).classes(
                                    "premium-button"
                                )

                    # ----------------------------------------
                    # RENDER NOTE
                    # ----------------------------------------

                    def render_note(note):

                        note_id = note.get("id")

                        with ui.card().classes(
                            "note-card"
                        ):

                            with ui.row().classes(
                                "w-full items-start justify-between"
                            ):

                                with ui.column().classes(
                                    "gap-2"
                                ):

                                    ui.label(
                                        note.get(
                                            "title",
                                            "Untitled Meeting",
                                        )
                                    ).classes(
                                        "note-title"
                                    )

                                    meeting_date = (
                                        note.get(
                                            "meeting_date"
                                        )
                                        or "No date"
                                    )

                                    ui.label(
                                        meeting_date
                                    ).classes(
                                        "meta-text"
                                    )

                                delete_button = ui.button(
                                    icon="delete_outline"
                                ).props(
                                    "flat round"
                                ).classes(
                                    "delete-button"
                                )

                                delete_button.tooltip(
                                    "Delete note"
                                )

                                def open_delete_dialog(
                                    current_note_id=note_id,
                                ):

                                    note_id_to_delete[
                                        "value"
                                    ] = current_note_id

                                    delete_dialog.open()

                                delete_button.on(
                                    "click",
                                    open_delete_dialog,
                                )

                            content = (
                                note.get("content")
                                or ""
                            )

                            preview = content

                            if len(preview) > 280:

                                preview = (
                                    preview[:280]
                                    + "..."
                                )

                            ui.label(
                                preview
                            ).classes(
                                "note-preview mt-5"
                            )

                            if len(content) > 280:

                                with ui.expansion(
                                    "Read full note"
                                ).classes(
                                    "w-full mt-4"
                                ):

                                    ui.label(
                                        content
                                    ).classes(
                                        "note-preview"
                                    )

                    # ----------------------------------------
                    # LOAD NOTES
                    # ----------------------------------------

                    def load_notes():

                        notes_container.clear()

                        try:

                            notes = get_notes(
                                project_id
                            )

                            if not notes:

                                with notes_container:

                                    with ui.column().classes(
                                        "empty-state items-center justify-center"
                                    ):

                                        ui.html(
                                            """
                                            <div class="empty-mark">
                                                <span class="material-icons">
                                                    description
                                                </span>
                                            </div>
                                            """
                                        )

                                        ui.label(
                                            "No meeting notes yet"
                                        ).classes(
                                            "section-heading"
                                        )

                                        ui.label(
                                            "Add your first meeting note to begin building intelligence around this project."
                                        ).classes(
                                            "page-subtitle mt-2"
                                        )

                                        ui.button(
                                            "Add Meeting Note",
                                            on_click=note_dialog.open,
                                        ).classes(
                                            "premium-button mt-5"
                                        )

                                return

                            with notes_container:

                                for note in notes:

                                    render_note(
                                        note
                                    )

                        except requests.RequestException as error:

                            with notes_container:

                                ui.label(
                                    f"Could not load meeting notes: {error}"
                                ).classes(
                                    "note-preview"
                                )

                    load_notes()

                # ============================================
                # ASK AI
                # ============================================

                with ui.tab_panel(
                    ai_tab
                ).classes(
                    "p-0 pt-10"
                ):

                    with ui.column().classes(
                        "ai-shell"
                    ):

                        with ui.column().classes(
                            "chat-scroll w-full"
                        ) as chat_container:

                            def add_welcome():

                                with ui.column().classes(
                                    "ai-response gap-4"
                                ):

                                    with ui.row().classes(
                                        "items-center gap-3"
                                    ):

                                        ui.html(
                                            """
                                            <div class="ai-avatar">
                                                <span class="material-icons" style="font-size:15px">
                                                    auto_awesome
                                                </span>
                                            </div>
                                            """
                                        )

                                        ui.label(
                                            "MeetIntel AI"
                                        ).classes(
                                            "ai-name"
                                        )

                                    ui.label(
                                        "Ask anything about the meetings in this project. I will search the relevant context and give you a focused answer."
                                    ).classes(
                                        "ai-answer"
                                    )

                            add_welcome()

                        with ui.row().classes(
                            "ai-input-area w-full items-center gap-3"
                        ):

                            question_input = ui.input(
                                placeholder="Ask anything about your meetings..."
                            ).classes(
                                "ask-input flex-grow"
                            )

                            send_button = ui.button(
                                icon="arrow_upward"
                            ).classes(
                                "send-button"
                            )

                            loading = ui.row().classes(
                                "items-center gap-2"
                            )

                            loading.set_visibility(
                                False
                            )

                            with loading:

                                ui.spinner(
                                    size="18px",
                                )

                                ui.label(
                                    "Analyzing your meeting intelligence..."
                                ).classes(
                                    "loading-text"
                                )

                            async def submit_question():

                                question = (
                                    question_input.value
                                    or ""
                                ).strip()

                                if not question:
                                    return

                                question_input.value = ""

                                with chat_container:

                                    with ui.column().classes(
                                        "w-full mb-8"
                                    ):

                                        ui.label(
                                            question
                                        ).classes(
                                            "user-question"
                                        )

                                loading.set_visibility(
                                    True
                                )

                                send_button.disable()

                                try:

                                    result = await run.io_bound(
                                        ask_ai,
                                        project_id,
                                        question,
                                    )

                                    answer = (
                                        result.get(
                                            "answer"
                                        )
                                        or "I could not generate an answer."
                                    )

                                    sources = (
                                        result.get(
                                            "sources"
                                        )
                                        or []
                                    )

                                    with chat_container:

                                        with ui.column().classes(
                                            "ai-response gap-4 mb-10"
                                        ):

                                            with ui.row().classes(
                                                "items-center gap-3"
                                            ):

                                                ui.html(
                                                    """
                                                    <div class="ai-avatar">
                                                        <span class="material-icons" style="font-size:15px">
                                                            auto_awesome
                                                        </span>
                                                    </div>
                                                    """
                                                )

                                                ui.label(
                                                    "MeetIntel AI"
                                                ).classes(
                                                    "ai-name"
                                                )

                                            ui.label(
                                                answer
                                            ).classes(
                                                "ai-answer"
                                            )

                                            if sources:

                                                with ui.column().classes(
                                                    "source-box gap-2"
                                                ):

                                                    ui.label(
                                                        "Sources"
                                                    ).classes(
                                                        "source-title"
                                                    )

                                                    for source in sources:

                                                        note_id = source.get(
                                                            "meeting_note_id",
                                                            "—",
                                                        )

                                                        chunk_index = source.get(
                                                            "chunk_index",
                                                            "—",
                                                        )

                                                        ui.label(
                                                            f"Meeting Note #{note_id} · Discussion {chunk_index}"
                                                        ).classes(
                                                            "source-item"
                                                        )

                                except requests.RequestException as error:

                                    with chat_container:

                                        with ui.column().classes(
                                            "ai-response gap-3 mb-8"
                                        ):

                                            ui.label(
                                                "Unable to reach MeetIntel AI."
                                            ).classes(
                                                "ai-name"
                                            )

                                            ui.label(
                                                str(error)
                                            ).classes(
                                                "meta-text"
                                            )

                                finally:

                                    loading.set_visibility(
                                        False
                                    )

                                    send_button.enable()

                                    question_input.run_method(
                                        "focus"
                                    )

                            send_button.on(
                                "click",
                                submit_question,
                            )

                            question_input.on(
                                "keydown.enter",
                                submit_question,
                            )


# ============================================================
# APPLICATION
# ============================================================

ui.run(
    title="MeetIntel AI",
    port=8080,
    reload=False,
)