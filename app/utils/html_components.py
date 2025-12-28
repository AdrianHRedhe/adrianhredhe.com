from jinja2 import Template

HEADER_TEMPLATE = """
<header class="site-header">
    <div class="container">
        <pre class="logo-ascii">{{ name }}</pre>
        <nav>
            <ul>
                {% for label, url in links %}
                <li><a href="{{ url }}">{{ label }}</a></li>
                {% endfor %}
            </ul>
        </nav>
    </div>
</header>
"""


def get_ascii_art_name():
    try:
        with open("app/static/logo.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "AdrianHRedhe"


LOGO_ASCII = get_ascii_art_name()


def get_header(links=None):
    name = LOGO_ASCII
    if links is None:
        links = [
            ("Home", "/"),
            # ("Blog", "/blog"),
            # ("About", "/about"),
            # ("Projects", "/projects"),
        ]

    template = Template(HEADER_TEMPLATE)
    return template.render(name=name, links=links)


def add_header(page_content, links=None):
    header = get_header(links)
    html = f"{header}<main>{page_content}</main>"
    return html
