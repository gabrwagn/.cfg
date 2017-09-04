#!/usr/bin/python

from datetime import datetime

now = datetime.now()
time = now.strftime('%H:%M')

print(time)
