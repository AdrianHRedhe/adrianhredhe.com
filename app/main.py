import os
from markdown import markdown
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, Response
from pydantic import BaseModel
from app.utils.render_markdown import render_markdown

app = FastAPI()


class Input(BaseModel):
    name: str


class Output(BaseModel):
    greeting: str


#@app.get("/")
#def home():
#    return {"health_check": "OK"}


@app.get("/", response_class=HTMLResponse)
def readme():
    html = render_markdown("README.md", {"creator": "Adrian"})

    blogposts = os.listdir("app/templates")
    table_of_contents_blog = "### Blogposts:"

    for post in blogposts:
        table_of_contents_blog += f"\n* [{post}](/blog/{post})"

    html += markdown(table_of_contents_blog)
    return html


@app.get("/blog/{blog_post_name}", response_class=HTMLResponse)
def get_markdown_blog(blog_post_name):
    html = render_markdown(f"app/templates/{blog_post_name}")
    return html


@app.post("/api", response_model=Output)
def predict(payload: Input):
    greeting = f"Hello {payload.name}"
    return {"greeting": greeting}
