from modules import art
import random
import sys
from unicodedata import name

'''
    Characters from https://en.wikipedia.org/wiki/Code_page_437

    ░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
    · ∙ ° ° • . * 

    ┌─┬─┐
    │ │ │
    ├─┼─┤
    └─┴─┘
    '''


def mainscreen():
    rand = random.randrange(1, 3)
    match rand:
        case 1:
            mainscreen1()
        case 2:
            mainscreen2()


def mainscreen1():
    art.cd(226, '', "   ______________    ____     __________  ________ __", '', True)
    art.cd(226, '', "  / ___/_  __/   |  / __ \   /_  __/ __ \/ ____/ //_/", '', True)
    art.cd(226, '', "  \__ \ / / / /| | / /_/ /    / / / /_/ / __/ / ,<   ", '', True)
    art.cd(226, '', " ___/ // / / ___ |/ _, _/    / / / _, _/ /___/ /| |  ", '', True)
    art.cd(226, '', "/____//_/ /_/  |_/_/ |_|    /_/ /_/ |_/_____/_/ |_|  ", '', True)
    art.cd(13, '', "[Pause]", '', True)
    input("")


def mainscreen2():
    #
    # Row 1
    #
    art.cd(0, 0, "  ", '', False)
    art.cd(15, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(15, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(15, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(15, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(15, 0, ".", '', False)  # star
    art.cd(0, 0, "         ", '', False)
    art.cd(15, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(15, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(15, 0, "*", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    # ░ ▒ ▓ █ ▄ ▀ ■ ▌▐
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 27, "▄", '', False)

    # ░ ▒ ▓
    art.cd(27, 27, "░░░░▒░░▒▒░", '', False)
    art.cd(4, 4, "  ", '', False)
    art.cd(27, 27, "▓", '', False)
    art.cd(27, 27, "▒", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(27, 27, "▒", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(27, 27, "▒", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(4, 4, " ", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(27, 27, "▒", '', False)
    art.cd(27, 27, "▒", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(27, 27, "▒", '', False)
    art.cd(27, 27, "▒", '', False)
    art.cd(27, 27, "░", '', False)
    art.cd(27, 27, "▒", 0, True)
