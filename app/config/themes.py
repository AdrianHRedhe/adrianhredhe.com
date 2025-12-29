def get_theme(theme):
    themes = {
        "yellow": {"accent": "#ffd166"},
        "cyan": {"accent": "#95e6cb"},
        "red": {"accent": "#F23C16"},
        "blue": {"accent": "#4fc3ff"},
        "purple": {"accent": "#bf8eff"},
    }
    return themes.get(theme)
