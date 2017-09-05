## colorize

### Python printing in color made simple.

This module consists of one function called `print_color()` that allows
you to print something in a different format or color in Python.
It allows you to change to foreground and background color of text in addition
to its format (bold, underscore, reverse_video)

There are 3 required keyword arguments that must be supplied that default to
`None` when missing. These keyword arguments are `format`, `foreground`, or
`background`.

A simple call works like this:

```python
from colorize import color_print

color_print("The Knights who say Ni!", format="bold",
            foreground="white", background="green")
```

In this call, the text is "The Knights who say Ni!" and it's formatted as
`bold`, has a foreground color of `white`, and a background color of
`green`.
