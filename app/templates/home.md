Hello i am {{creator}} and this is a small  
website were I keep some of my projects   
and other things that are handy for me.  

Get my setup from my [.dotfiles](https://github.com/AdrianHRedhe/.dotfiles.git)  
Will publish blogposts on the subject of this  
including but not limited to nvim, tmux and karabiner.

{% if blogposts %}
### Blogposts:
{% for post in blogposts %}
* [{{ post | replace('.md', '') }}](/blog/{{ post }})
{% endfor %}
{% endif %}
