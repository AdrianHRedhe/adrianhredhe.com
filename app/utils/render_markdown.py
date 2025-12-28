import markdown
from jinja2 import Template
from pygments.formatters import HtmlFormatter


def _load_static_assets():
    """Helper to load assets once."""
    # Get style for code highlighter
    formatter = HtmlFormatter(style="lightbulb", full=True, cssclass="codehilite")
    pygments_css = formatter.get_style_defs()

    # Load style for everything else
    try:
        with open("app/static/style.css", "r") as f:
            style_css = f.read()
    except FileNotFoundError:
        style_css = ""

    return f"<style>{pygments_css}\n{style_css}</style>"


# Load css only once
CACHED_CSS = _load_static_assets()


def render_markdown(filename, variables=None):
    with open(filename, "r") as file:
        markdown_string = file.read()

    # Use jinja to render as template (can add variables)
    template = Template(markdown_string)
    rendered_md = template.render(variables or {})

    # Use markdown to convert to HTML
    html = markdown.markdown(rendered_md, extensions=["fenced_code", "codehilite"])

    return CACHED_CSS + html
