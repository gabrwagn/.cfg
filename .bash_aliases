# Custom aliases

alias ll='ls -la'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
alias wifi-list='nmcli d wifi list'
alias wifi-connect='nmcli d wifi connect'
alias byebye='shutdown now'
alias pythonenv='pipenv run python'

openstream() {
	livestreamer --twitch-oauth-token=p44pdrecof3j60qtjgc4twhycumh9g twitch.tv/$1 '1080p60,720p60,best';
}
openstream='openstream'
