## Blog
More to come here in the future.
As of now they are only placeholders
so that I can try out what they should
look like in the future.

{% if blogposts %}
### Blogposts:
{% for post in blogposts %}
* [{{ post | replace('.md', '') }}](/blog/{{ post }})
{% endfor %}
{% endif %}
