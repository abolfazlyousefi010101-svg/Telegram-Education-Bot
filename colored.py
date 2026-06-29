import os
import sys

if sys.platform.startswith("win"):
    os.system("")

class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class Color:
    RED    = "\033[31m"
    GREEN  = "\033[32m"
    YELLOW = "\033[33m"
    BLUE   = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN   = "\033[36m"
    WHITE  = "\033[37m"
    BLACK  = "\033[30m"

    BRIGHT_RED    = "\033[91m"
    BRIGHT_GREEN  = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE   = "\033[94m"
    BRIGHT_CYAN   = "\033[96m"

class BgColor:
    RED    = "\033[41m"
    GREEN  = "\033[42m"
    YELLOW = "\033[43m"
    BLUE   = "\033[44m"
    MAGENTA = "\033[45m"
    CYAN   = "\033[46m"
    WHITE  = "\033[47m"
    BLACK  = "\033[40m"

    BRIGHT_RED   = "\033[101m"
    BRIGHT_BLUE  = "\033[104m"
    BRIGHT_GREEN = "\033[102m"

def colored(text, color="", bg="", bold=False, underline=False):
    style = ""
    if bold:
        style += Style.BOLD
    if underline:
        style += Style.UNDERLINE
    style += color + bg
    return f"{style}{text}{Style.RESET}"

def success(text):
    return colored(text, Color.GREEN, bold=True)

def error(text):
    return colored(text, Color.RED, bold=True)

def warning(text):
    return colored(text, Color.YELLOW, bold=True)

def info(text):
    return colored(text, Color.BLUE, bold=True)

def title(text):
    return colored(text, Color.BRIGHT_BLUE, bold=True, underline=True)



