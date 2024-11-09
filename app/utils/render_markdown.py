# %%
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from jinja2 import Template

def render_markdown(filename, variables=None):
    with open(filename, "r") as file:
        markdown_string = file.read()
        # Use jinja to render as template (can add variables)
        template = Template(markdown_string)
        rendered_md = template.render(variables or {})
    
        
    # Use markdown to convert to HTML
    html = markdown.markdown(
        rendered_md, 
        extensions=["fenced_code", "codehilite"]
    )

    return html

render_markdown("README.md", {"creator": "Adrian"})
# %%
