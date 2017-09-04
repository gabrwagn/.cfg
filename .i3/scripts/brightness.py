#!/usr/bin/env python

import os

output = ' '

path = os.path.join('/sys', 'class', 'backlight', 'intel_backlight')
brightness = 0
max_brightness = 0

with open(os.path.join(path, 'brightness'), 'r') as fb:
    brightness = fb.readline()

with open(os.path.join(path, 'max_brightness'), 'r') as fb:
    max_brightness = fb.readline()

percent = float(brightness)/float(max_brightness)

output += str(int(percent * 100)) + '%'

print(output)
