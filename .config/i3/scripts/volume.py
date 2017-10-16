#!/usr/bin/python3

import subprocess
from subprocess import PIPE
import os

command = ['amixer','sget', 'Speaker']
p = subprocess.Popen(command, stdout=PIPE, stderr=PIPE)
output, err = p.communicate()

lines = str(output).split('\\n')
speaker = lines[-2].replace('[', '').replace(']', '')

volume = int(speaker.split(' ')[-3].replace('%', ''))
status = speaker.split(' ')[-1]

output = ""
color = ''

if status == 'on':
    if volume > 50:
        output = ' '
    elif volume > 1:
        output = ' '
    else:
        output = ' '

    bars = int(volume * 5 / 100)
    output += 'l'*bars
else:
    output = ''
    color = '#FF0000'

print(output)
print(output)
print(color)

