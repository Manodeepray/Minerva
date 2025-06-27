from rich.console import Console
from rich.text import Text

def print_logo():

    console = Console()


    """https://patorjk.com/text-color-fader/"""

    ascii_art_1 = """\
    ███╗   ███╗██╗███╗   ██╗███████╗██████╗ ██╗   ██╗ █████╗     
    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗██║   ██║██╔══██╗    
    ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝██║   ██║███████║    
    ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══██║    
    ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║ ╚████╔╝ ██║  ██║    
    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝      
    """



    ascii_art_2 = """
    ░  ░░░░  ░░        ░░   ░░░  ░░        ░░       ░░░  ░░░░  ░░░      ░░░░░░░░
    ▒   ▒▒   ▒▒▒▒▒  ▒▒▒▒▒    ▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒▒▒▒▒▒
    ▓        ▓▓▓▓▓  ▓▓▓▓▓  ▓  ▓  ▓▓      ▓▓▓▓       ▓▓▓▓  ▓▓  ▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓
    █  █  █  █████  █████  ██    ██  ████████  ███  █████    ████        ███████
    █  ████  ██        ██  ███   ██        ██  ████  █████  █████  ████  ███████
                                                                                \n
    """
    
    # Gradient colors from pink to blue
    gradient = ["#ff77ff", "#cc66ff", "#9966ff", "#6666ff", "#3399ff", "#00ccff", "#00ffff"]

    # Split into lines
    lines = ascii_art_1.splitlines()

    colored_lines = []

    for i, line in enumerate(lines):
        color = gradient[i * len(gradient) // len(lines)]
        colored_lines.append(Text(line, style=color))

    for line in colored_lines:
        console.print(line)

def print_description():
    console = Console()
    
    gradient = ["#ff77ff", "#cc66ff", "#9966ff", "#6666ff", "#3399ff", "#00ccff", "#00ffff"]

    ascii_art_3 = """
                    ┌┬┐┬┌┐┌┌─┐┬─┐┬  ┬┌─┐  
    starting...     │││││││├┤ ├┬┘└┐┌┘├─┤  
                    ┴ ┴┴┘└┘└─┘┴└─ └┘ ┴ ┴  
    --- It explores. It strategizes. It acts. The autonomous Agent system for web app security.                                                  
                                                                                                                                                                                                                                                                        
    """

    lines = ascii_art_3.splitlines()

    colored_lines = []

    for i, line in enumerate(lines):
        color = gradient[i * len(gradient) // len(lines)]
        colored_lines.append(Text(line, style=color))

    for line in colored_lines:
        console.print(line)
# print_description()
# print_logo()