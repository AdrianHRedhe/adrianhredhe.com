import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.utils.render_markdown import render_markdown

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


class Input(BaseModel):
    name: str


class Output(BaseModel):
    greeting: str


@app.get("/", response_class=HTMLResponse)
def home():
    blogposts = os.listdir("app/templates/blogposts")
    html = render_markdown(
        "home.md",
        {
            "creator": "Adrian",
            "blogposts": blogposts,
        },
    )
    return html


@app.get("/blog/{blog_post_name}", response_class=HTMLResponse)
def get_markdown_blog(blog_post_name):
    html = render_markdown(f"blogposts/{blog_post_name}")
    return html


@app.post("/api", response_model=Output)
def predict(payload: Input):
    greeting = f"Hello {payload.name}"
    return {"greeting": greeting}
