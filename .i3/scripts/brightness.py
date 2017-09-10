#!/usr/bin/python3

import os

output = ' '
color = ''
path = os.path.join('/sys', 'class', 'backlight', 'intel_backlight')
brightness = 0
max_brightness = 0

with open(os.path.join(path, 'max_brightness'), 'r') as fb:
    max_brightness = float(fb.readline())

with open(os.path.join(path, 'brightness'), 'r') as fb:
    brightness = min(float(fb.readline()), max_brightness / 2)

percent = int(100 * float(brightness)/float(max_brightness))

output += 'l'*(int(10 * percent / 100))

print(output)
print(output)
print(color)
