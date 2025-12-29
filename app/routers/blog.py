import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from app.utils.render_markdown import render_markdown

router = APIRouter()


@router.get("/{blog_post_name}", response_class=HTMLResponse)
def get_markdown_blog(blog_post_name):
    template_path = f"blogposts/{blog_post_name}"
    file_path = f"app/templates/{template_path}"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="blogpost not found",
        )
    html = render_markdown(template_path)
    return html
