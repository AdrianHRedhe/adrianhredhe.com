def get_theme(theme):
    themes = {
        "yellow": {"accent": "#ffd166", "favicon": "favicon-yellow.png"},
        "cyan": {"accent": "#95e6cb", "favicon": "favicon-cyan.png"},
        "red": {"accent": "#F23C16", "favicon": "favicon-red.png"},
        "blue": {"accent": "#4fc3ff", "favicon": "favicon-blue.png"},
        "purple": {"accent": "#bf8eff", "favicon": "favicon-purple.png"},
    }
    return themes.get(theme)
