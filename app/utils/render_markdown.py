# %%
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from pygments import formatter
from pygments.formatters import HtmlFormatter
from jinja2 import Template


def format_html(html):

    # General Markdown Formatter
    #    md_css_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/4.0.0/github-markdown.min.css">'

    # Custom code highlight functionality
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()

    # add some custom formatting
    custom_css = """
    .codehilite pre {
        background-color: #f6f8fa; /* Light grey background (typical Markdown style) */
        color: #333333; /* Dark text color for better readability */
    }
    .codehilite code {
        background-color: transparent; /* No background for inline code */
    }
    """
    css_string += custom_css
    md_css_string = f"<style>{css_string}</style>"

    # return md_css_link + md_css_string + html
    return md_css_string + html


def render_markdown(filename, variables=None):
    with open(filename, "r") as file:
        markdown_string = file.read()
        # Use jinja to render as template (can add variables)
        template = Template(markdown_string)
        rendered_md = template.render(variables or {})

    # Use markdown to convert to HTML
    html = markdown.markdown(rendered_md, extensions=["fenced_code", "codehilite"])

    # Format HTML
    formatted_html = format_html(html)

    return formatted_html


# render_markdown("app/templates/simpe_with_code.md", {"creator": "Adrian"})
# %%
