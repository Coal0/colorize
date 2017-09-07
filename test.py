from colorize import print_color

colors = [
    'black', 'red', 'green','yellow',
    'blue','magenta', 'cyan','white',
    ]

for fg in colors:
    for bg in colors:
        print_color("The Knights who say Ni!", foreground=fg, background=bg, format='bold')
