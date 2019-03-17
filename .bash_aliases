# Custom aliases

alias ll='ls -la'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
alias byebye='systemctl suspend'
alias pythonenv='pipenv run python'
alias ranger='ranger --choosedir=$HOME/rangerdir; LASTDIR=`cat $HOME/rangerdir`; cd "$LASTDIR"'
alias sudo='sudo -E'
alias torrentsweep='mv ~/docs/downloads/*.torrent ~/docs/torrents/.torrent/'
alias proj='cd ~/docs/projects; ranger'
alias bm='bashmount'
alias wow='wine .wine/drive_c/Program\ Files/World\ of\ Warcraft\ 1.12/WoW.exe'
alias bt="bluetoothctl"

# SHAME ON YOU, USE ABSOLUTE PATHS, THIS IS YOUR PUNISHMENT
alias rm='rm -i'
