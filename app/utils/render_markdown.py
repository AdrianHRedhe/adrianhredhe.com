from functools import lru_cache

import markdown
from fastapi.templating import Jinja2Templates
from pygments.formatters import HtmlFormatter


@lru_cache()
def get_pygments_css():
    return HtmlFormatter(style="lightbulb").get_style_defs(".codehilite")


@lru_cache()
def get_templates():
    return Jinja2Templates(directory="app/templates")


def render_markdown(template_path, variables=None):
    templates = get_templates()

    # Use jinja to render as template (can add variables)
    md_template = templates.get_template(template_path)
    rendered_md = md_template.render(variables or {})

    # Convert markdown to html and use extensions for highlighting code in code blocks
    html_body = markdown.markdown(rendered_md, extensions=["fenced_code", "codehilite"])

    pygments_css = get_pygments_css()

    full_html_template = templates.get_template("base.html")

    # Finally use templates once again but for returning page
    return full_html_template.render(
        {
            "content": html_body,
            "pygments_css": pygments_css,
        },
    )
