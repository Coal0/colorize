"""
Provides a simple wrapper function of print that allows
you to print with a different format.

You can change the attribute, the foreground color, and
the background color.

By: Asad Moosvi
"""

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

    ansi_escape_seq = "\033[{format_codes}m"
    format_codes = ''

    # if no format/attribute is specified for the ansi escape sequence
    # then default to no attribute otherwise set the repective attribute
    if not format:
        format_codes += '0'
    else:
        if format == 'bold':
            format_codes += '1'
        elif format == 'underscore':
            format_codes += '4'
        elif format == 'reverse_video':
            format_codes += '7'
        else:
            format_codes += '0'

    # set foreground if any supplied
    if foreground:
        foreground = foreground.strip().lower()
        foreground_codes = {
            'black': ';30',
            'red': ';31',
            'green': ';32',
            'yellow': ';33',
            'blue': ';34',
            'magenta': ';35',
            'cyan': ';36',
            'white': ';37'
            }

        if foreground in foreground_codes:
            format_codes += foreground_codes[foreground]

    # set background if any supplied
    if background:
        if not foreground:
            format_codes += ';'

        background = background.strip().lower()
        background_codes = {
            'black': ';40',
            'red': ';41',
            'green': ';42',
            'yellow': ';43',
            'blue': '44',
            'magenta': ';45',
            'cyan': ';46',
            'white': ';47'
            }

        if background in background_codes:
            format_codes += background_codes[background]

    ansi_escape_seq = ansi_escape_seq.format(format_codes=format_codes)
    ansi_escape_seq_end = "\033[0m"

    all_strings = [str(s) for s in print_args]

    if 'sep' in print_kwargs:
        print('sep => {}'.format(print_kwargs['sep']))
        print_string = print_kwargs['sep'].join(all_strings)
    else:
        print_string = ' '.join(all_strings)

    print(ansi_escape_seq + print_string + ansi_escape_seq_end, **print_kwargs)
