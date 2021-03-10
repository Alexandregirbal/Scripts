from enum import Enum

class Colors(Enum):
    Black = 30
    Red = 31
    Green = 32
    Yellow = 33
    Blue = 34
    Magenta = 35
    Cyan = 36
    White = 37

def colorize(string, color):
    return f"\x1b[{color.value}m{string}\x1b[0m"

def clearConsole():
    print("\033c")

#TEST
if __name__ == '__main__':
    for color in Colors:
        print(colorize(color.name,color))