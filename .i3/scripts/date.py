#!/usr/bin/python

from datetime import datetime

now = datetime.now()
date = now.strftime('%a %b, %d')

print(date)
