## Projects

{% if projects %}
{% for project in projects %}
* [{{ project | replace('.md', '') }}](/projects/{{ project | replace('.md', '') }})
{% endfor %}
{% endif %}
