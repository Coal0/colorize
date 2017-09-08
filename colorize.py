#!/usr/bin/env python3

"""
Provides a simple wrapper function of print that allows
you to print in a different format and color.

You can change the attribute, the foreground color, and
the background color of text when printing.

By: Asad Moosvi
"""

import argparse
import sys

COLORS = {
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
    None: 39 # default foreground
    }

FORMATS = {
    'bold': 1,
    'faint': 2,
    'italic': 3,
    'underline': 4,
    'underscore': 4,
    'reverse_video': 7,
    'strikeout': 9,
    'frame': 51,
    'overline': 53
}

ANSI_ESCAPE_SEQ = "\033[{}m"
ANSI_ESCAPE_SEQ_END = "\033[0m"

def idiot_check(label, value, dictionary, add=0):
    if value:
        value = value.strip().lower()

    if value.startswith('#'):
        return [38+add, 2, int(value[1:3], 16), int(value[3:5], 16), int(value[5:7], 16)]
    if value not in dictionary:
        raise ValueError('invalid {} color {!r}. Must be one of {}'.format(label, value, list(dictionary.keys())))
    return [dictionary[value]+add]


def print_color(*print_args, format=None, foreground=None,
        background=None, **print_kwargs):
    """A wrapper around the print function used for printing with different
    format, foreground, and background options.

    param format: (default=None)
        By default the there is no format set. There are 3 possible format modes
        available: bold, underscore or reverse_video
        bold: make text bold
        underscore: underline text
        reverse_video: switch the colors of text background and foreground

    param foreground: (default=None)
        This parameter allows you to set the forground color of the text.
        Available options are: black, red, green, yellow, blue,
        magenta, cyan, and white.

    param background: (default=None)
        This parameter allows you to set the background color of the text.
        The available options are the same as foreground color.

    Example usecase:
        print_color('hello world', format='bold', foreground='green')
        This prints `hello world` in bold and green foreground color.
    """
    sep = print_kwargs.pop('sep', ' ')

    # if no format/attribute is specified for the ansi escape sequence
    # then default to no attribute otherwise set the repective attribute
    format_codes =[]
    if format:
        format_codes += sum((idiot_check('format', x, FORMATS) for x in format.split()), [])

    format_codes += idiot_check('foreground', foreground, COLORS)

    format_codes += idiot_check('background', background, COLORS, add=10)

    ansi_escape_seq = ANSI_ESCAPE_SEQ.format(';'.join(map(str, format_codes)))

    print_string = sep.join(map(str, print_args))
    print(ansi_escape_seq + print_string + ANSI_ESCAPE_SEQ_END, **print_kwargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='format and color text '
                                                 'read from stdin')
    parser.add_argument('-fg', '--foreground')
    parser.add_argument('-bg', '--background')
    parser.add_argument('-fmt', '--format')

    args = parser.parse_args()
    user_input = sys.stdin.read().rstrip()
    print_color(user_input, format=args.format,
                foreground=args.foreground,
                background=args.background)
