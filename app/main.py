import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.config.themes import get_theme
from app.routers import api, blog, projects, services
from app.utils.render_markdown import render_markdown

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(blog.router, prefix="/blog", tags=["blog"])
app.include_router(api.router, prefix="/api", tags=["api"])
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])


@app.get("/", response_class=HTMLResponse)
def home():
    blogposts = blog.sort_blogposts(os.listdir("app/templates/blogposts"))
    projects = os.listdir("app/templates/projects")
    services = os.listdir("app/templates/services")
    html = render_markdown(
        "home.md",
        {
            "creator": "Adrian",
            "blogposts": blogposts,
            "projects": projects,
            "services": services,
            "theme": get_theme("yellow"),
        },
    )
    return html
