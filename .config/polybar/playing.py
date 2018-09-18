#!/usr/bin/env python

import subprocess
import re

def main():
    # run mpc to get song info and
    cmd = "mpc"
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    output, error = process.communicate()
    output = output.decode('utf-8')

    # format:
    # song
    # [status] #n/total played/totaltime (%)
    # vol repeat random single consume

    # only true if song is currently playing
    lines = output.split('\n')
    if len(lines) > 3:
        # get song and artis
        song_artist = lines[0].split(' - ')

        # reconstruct song name (if it contains multiple -)
        song = song_artist[1]
        for rest in song_artist[2:]:
            song += ':' + rest

        # get artist name, end short if too long
        max_len = 25
        artist = song_artist[0]
        if len(artist) > max_len + 4:
            artist = artist[:max_len] + '...'

        # extract status
        status = lines[1].split(' ')[0]
        # build msg
        prompt = '{}  {} - {}'.format(get_icon(status), song.lower(), artist.lower())
        print(prompt)
    else:
        cmd = "org.freedesktop.DBus.Properties.Get"
        domain = "org.mpris.MediaPlayer2"
        path = "/org/mpris/MediaPlayer2"

        full = "dbus-send --print-reply --dest={}.spotify \
            {} {} string:{}.Player string:Metadata".format(domain, path, cmd, domain)

        process = subprocess.Popen(full.split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        output, error = process.communicate()
        output = output.decode('UTF-8')

        if len(output):
            artist_pattern = re.compile('"xesam:artist"\n.+\n.+', re.MULTILINE)
            s = re.search(artist_pattern, output)
            artist = s.group(0).split('\n')[2]
            artist = artist[artist.index('"')+1:-1]

            song_pattern = re.compile('"xesam:title"\n.+', re.MULTILINE)
            s = re.search(song_pattern, output)
            song = s.group(0).split('\n')[1]
            song = song[song.index('"')+1:-1]

            cmd = "playerctl -p spotify status"
            process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            output = output.decode('unicode_escape').rstrip()
            status = "[{}]".format(output.lower())
            icon = get_icon(status)
            print('{}  {} - {}'.format(icon, artist.lower(), song.lower()))
        else:
            print("")

def get_icon(status):
    # get icon based on status
    if status == "[playing]":
        return ""
    elif status == "[paused]":
        return ""
    else:
        return ""

if __name__ == '__main__':
    main()

