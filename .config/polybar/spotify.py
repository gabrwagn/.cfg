#!/usr/bin/python

import subprocess
import re


def main():
    cmd = "org.freedesktop.DBus.Properties.Get"
    domain = "org.mpris.MediaPlayer2"
    path = "/org/mpris/MediaPlayer2"

    full = "dbus-send --print-reply --dest={}.spotify \
        {} {} string:{}.Player string:Metadata".format(domain, path, cmd, domain)

    process = subprocess.Popen(full.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode('unicode_escape')

    if len(output):
        artist_pattern = re.compile('"xesam:artist"\n.+\n.+', re.MULTILINE)
        s = re.search(artist_pattern, output)
        artist = s.group(0).split('\n')[2]
        artist = artist[artist.index('"')+1:-1]

        song_pattern = re.compile('"xesam:title"\n.+', re.MULTILINE)
        s = re.search(song_pattern, output)
        song = s.group(0).split('\n')[1]
        song = song[song.index('"')+1:-1]

        icon = get_icon()
        print('{}  {} - {}'.format(icon, artist, song))
    else:
        print("")


def get_icon():
    full = "playerctl -p spotify status"
    process = subprocess.Popen(full.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode('unicode_escape').lower().strip()

    if output == "playing":
        return ""
    elif output == "paused":
        return ""
    else:
        return ""


if __name__ == "__main__":
    main()
