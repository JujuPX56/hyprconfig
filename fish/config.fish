if status is-interactive
    # Commands to run in interactive sessions can go here
    eval "$(starship init fish)"
    thefuck --alias f | source

    set -g fish_greeting

    set -U fish_user_paths $HOME/.local/bin $fish_user_paths
    export LIBVIRT_DEFAULT_URI="qemu:///system"

    alias ls="eza -1 --icons=always --show-symlinks"
    alias la="eza -1 --icons=always --show-symlinks --all"
    alias fuckoff="poweroff"
    alias code="exec code"
end

fish_add_path /home/jujupx/.spicetify
