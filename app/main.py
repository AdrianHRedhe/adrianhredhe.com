import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.config.themes import get_theme
from app.routers import api, blog
from app.utils.render_markdown import render_markdown

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(blog.router, prefix="/blog", tags=["blog"])
app.include_router(api.router, prefix="/api", tags=["api"])


@app.get("/", response_class=HTMLResponse)
def home():
    blogposts = os.listdir("app/templates/blogposts")
    html = render_markdown(
        "home.md",
        {
            "creator": "Adrian",
            "blogposts": blogposts,
            "theme": get_theme("yellow"),
        },
    )
    return html
