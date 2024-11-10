# %%
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, Response
from pydantic import BaseModel
from app.utils.render_markdown import render_markdown

app = FastAPI()


class Input(BaseModel):
    name: str


class Output(BaseModel):
    greeting: str


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.get("/readme", response_class=HTMLResponse)
def readme():
    html = render_markdown("README.md", {"creator": "Adrian"})

    html = render_markdown("app/templates/simpe_with_code.md")
    return html


@app.get("/blog/{blog_post_name}", response_class=HTMLResponse)
def get_markdown_blog(blog_post_name):
    html = render_markdown(f"app/templates/{blog_post_name}")
    return html


# @app.get("/readme2", response_class=Response)
# def readme2():
#     md = "README.md"
#     with open(md, "r") as file:
#         return Response(content=file.read(), media_type="text/markdown")
#
#
@app.post("/api", response_model=Output)
def predict(payload: Input):
    greeting = f"Hello {payload.name}"
    return {"greeting": greeting}
