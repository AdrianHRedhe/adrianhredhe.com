# Dotfiles - What, Why and How

## What ?
Dotfiles is a name for config files usually starting with . e.g.
.zshrc, .gitconfig. A lot of them also follow the pattern of
.config/nvim or .config/kitty

In general these allow for setting up your own specialized 
environment in the terminal, although some might have
consequences outside of the terminal as well.

## Why ?
The reason for saving all of these is to be able to comfortably
setup the environment which I like on any computer at any time
given just a few minutes.

Having a nice and workable environment makes coding a lot more
fun, but it is also makes me better at what I do. Both since I
am the primary user of what I config, I can really tighten the
loop between building new things and getting feedback on them.
It keeps me on my toes, and I generally strive to remove any
sense of discomfort as soon as I can.

Furthermore, keeping dotfiles in one central repo makes it worth
it and lovers the bar of making changes, since I will then easily have this change replicated across both home and work computers simultaneously if I so want to.

## How ?
If you just want to version control a few dotfiles on one computer it might be enough to use symlinks. That means having your dotfiles in one directory but have a reference in their regular locations pointing to your dotfile repository. This allows for version control of several files in different locations in one repository.

To make many dotfiles manageable over several computers I can't stress enough how much I recommend GNU Stow. Stow is a symlink farm manager which creates symlinks to all files in the repo you are currently in.

Say you have a directory / repo with the following structure:
```md
.
├── .gitconfig
└── .config
    └── karabiner
        └── karabiner.json
```

If you simply run:
```bash
stow .
```

It will use the current directory that you are in and generate symlinks to these files to the default target location which is the parent directory of the stow directory. As long as you put your dotfiles repo in the $HOME / ~ directory then you will get the symlinks put into $HOME / ~. That means that you will replicate what is in you repo in your home directory. So you will get `~/.gitconfig` and `~/.config/karabiner/karabiner.json` replicated with a symlink to your directory / repo. And if you make changes to these files e.g. `~/.gitconfig` then these changes will also be changed in dotfiles/.gitconfig and are then easily version controlled.

If you already have these files in place then stow wont automatically overwrite them. There is however a way to put what you already have in your home repository using:
```bash
stow --adopt .
```

If you already have a `~/.gitconfig` on your computer then you will overwrite `~/dotfiles/.gitconfig` with this option. This might be nice if you are either starting up with your dotfiles, or if you want to keep existing settings for this computer on a specific branch. I am more likely to want to overwrite something preexisting such as `~/.zshrc` in cases like this, I would use the `--adopt` flag, but then use git restore on this change, to revert it back to what it was in the current state of the repo.

### One more advanced trick
To keep it modular, I break down my dotfiles repo by computer, and then into packages. Allowing me to only install my kitty config but not my tmux config if I want to. It looks something like this (output slightly pruned):
```md
.dotfiles
├── .gitignore
├── mac
│   ├── .install-mac.sh
│   ├── git
│   │   ├── .config
│   │   └── .gitconfig
│   ├── hammerspoon
│   ├── karabiner
│   ├── kitty
│   ├── nvim
│   ├── ruff
│   ├── shell
│   │   ├── .inputrc
│   │   ├── .local
│   │   └── .shell
│   ├── tmux
│   │   ├── .config
│   │   ├── .tmux
│   │   └── .tmux.conf
│   ├── vim
│   │   ├── .vim
│   │   └── .vimrc
│   └── zsh
│       └── .zshrc
├── README.md
└── windows
    ├── bash
    │   └── .bashrc
    ├── nvim
    ├── shell
    ├── vim
    ├── vscode
    ├── windows_terminal
    └── zsh
        └── .zshrc
```

To only import the config for tmux I would run this command:
```bash
stow -d mac -t ~ tmux
```

Here the `-d` flag specifies that we will be using the `mac` as the stow directory, implicitly making `.dotfiles` the target directory. which is why we switch target by specifying the `-t` flag to change target to `~` / $HOME. Finally specifying tmux rather than . installs only that folder. 

If you are doing somthing like this, your packages, e.g. tmux / nvim etc look the way they should look from `~` inside the folders themselves. So if there should be a tmux related file in directory `~/my_folder/my_tmux_file` then `~/.dotfiles/mac/tmux` should have the file `~/.dotfiles/mac/tmux/my_folder/my_tmux_file`.

If you are looking for inspiration of general setup, or on specific setup for things like tmux / nvim / karabiner. Then you are very welcome to have a look at my [.dotfiles](https://github.com/AdrianHRedhe/.dotfiles.git) git repo.
