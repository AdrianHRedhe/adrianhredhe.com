Hello i am {{creator}} and this is a small website were I keep some 
of my projects and other things that are handy for me.  

Get my setup from my [.dotfiles](https://github.com/AdrianHRedhe/.dotfiles.git).
I will publish blogposts on the subject of tools and opinions including but not 
limited to nvim, tmux and karabiner.

Below are also some interactive projects and services I've built:

{% if projects %}
### Projects:
{% for project in projects %}
* [{{ project | replace('.md', '') }}](/projects/{{ project | replace('.md', '') }})
{% endfor %}
{% endif %}

{% if services %}
### Services:
{% for service in services %}
* [{{ service | replace('.md', '') }}](/services/{{ service | replace('.md', '') }})
{% endfor %}
{% endif %}

{% if blogposts %}
### Blogposts:
{% for post in blogposts %}
* [{{ post | replace('.md', '') }}](/blog/{{ post }})
{% endfor %}
{% endif %}
