import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from app.utils.render_markdown import render_markdown

router = APIRouter()

# Posts not listed here are appended alphabetically after these, in listing order.
BLOG_POST_ORDER = [
    "dotfiles_what_why_and_how.md",
    "csv2md_a_small_go_cli.md",
    "gwr_claims_bot_automating_delay_repay.md",
]


def sort_blogposts(blogposts):
    def sort_key(name):
        if name in BLOG_POST_ORDER:
            return (0, BLOG_POST_ORDER.index(name))
        return (1, name)

    return sorted(blogposts, key=sort_key)


@router.get("/", response_class=HTMLResponse)
def blog():
    blogposts = sort_blogposts(os.listdir("app/templates/blogposts"))
    html = render_markdown(
        "blog.md",
        {
            "blogposts": blogposts,
        },
    )
    return html


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
