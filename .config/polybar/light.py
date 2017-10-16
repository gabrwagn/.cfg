#!/usr/bin/python3

import subprocess
from subprocess import PIPE
import os

command = ['light']
p = subprocess.Popen(command, stdout=PIPE, stderr=PIPE)
output, err = p.communicate()

val = float(output.decode())

max_bars = 5
bars = min(int(max_bars * val / 50.0), max_bars)

print('-'*bars + '|')
