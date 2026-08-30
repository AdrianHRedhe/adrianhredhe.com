import os

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from app.config.themes import get_theme
from app.utils.render_markdown import render_markdown

router = APIRouter()

PROJECTS = [
    {"name": "Geolocalization Stockholm", "url": "/projects/geolocalization_stockholm"},
]


@router.get("/", response_class=HTMLResponse)
def projects_index():
    projects = os.listdir("app/templates/projects")
    html = render_markdown(
        "projects.md",
        {
            "projects": projects,
            "theme": get_theme("purple"),
        },
    )
    return html


@router.get("/geolocalization_stockholm", response_class=HTMLResponse)
def geolocalization_stockholm():
    html = render_markdown(
        "projects/geolocalization_stockholm.md",
        {"theme": get_theme("cyan")},
    )
    return html
