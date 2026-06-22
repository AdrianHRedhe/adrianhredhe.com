## Services

{% if services %}
{% for service in services %}
* [{{ service | replace('.md', '') }}](/services/{{ service | replace('.md', '') }})
{% endfor %}
{% endif %}
