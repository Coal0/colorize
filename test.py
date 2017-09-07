#!/usr/bin/env python3

from colorize import print_color

colors = [
    'black', 'red', 'green','yellow',
    'blue','magenta', 'cyan','white',
    ]

for fg in colors:
    for bg in colors:
        print_color("{} text on {} background".format(fg, bg), foreground=fg, background=bg, format='underline bold')
