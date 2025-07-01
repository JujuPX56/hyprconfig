if status is-interactive
    # Commands to run in interactive sessions can go here
    eval "$(starship init fish)"
    set -g fish_greeting

    alias ls="eza -1 --icons=always --show-symlinks"
    alias la="eza -1 --icons=always --show-symlinks --all"
end

fish_add_path /home/jujupx/.spicetify
