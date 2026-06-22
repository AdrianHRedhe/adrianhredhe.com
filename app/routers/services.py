import os

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from app.config.themes import get_theme
from app.services.plantstatus import get_grafana_url
from app.utils.render_markdown import render_markdown

router = APIRouter()

SERVICES = [
    {"name": "Plant Status", "url": "/services/plantstatus"},
]


@router.get("/", response_class=HTMLResponse)
def services_index():
    services = os.listdir("app/templates/services")
    html = render_markdown(
        "services.md",
        {
            "services": services,
            "theme": get_theme("blue"),
        },
    )
    return html


@router.get("/plantstatus", response_class=HTMLResponse)
def plantstatus():
    html = render_markdown(
        "services/plantstatus.md",
        {"grafana_url": get_grafana_url(), "theme": get_theme("green")},
    )
    return html
