import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.utils.html_components import add_header
from app.utils.render_markdown import render_markdown

app = FastAPI()


class Input(BaseModel):
    name: str


class Output(BaseModel):
    greeting: str


@app.get("/", response_class=HTMLResponse)
def home():
    blogposts = os.listdir("app/templates/blog")
    markdown_html = render_markdown(
        "app/templates/home.md",
        {
            "creator": "Adrian",
            "blogposts": blogposts,
        },
    )
    page_content = markdown_html
    html = add_header(page_content)
    return html


@app.get("/blog/{blog_post_name}", response_class=HTMLResponse)
def get_markdown_blog(blog_post_name):
    markdown_html = render_markdown(f"app/templates/blog/{blog_post_name}")
    html = add_header(markdown_html)
    return html


@app.post("/api", response_model=Output)
def predict(payload: Input):
    greeting = f"Hello {payload.name}"
    return {"greeting": greeting}
