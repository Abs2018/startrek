from modules import art
import random

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
    art.cd(13, '', "[Pause]", 0, True)
    input("")


def mainscreen2():
    '''
    white:
        dim: 244
        normal: 7
        Bright: 255
    blue:
        dim: 19
        normal: 4
        bright: 27
    '''

    #
    # Row 1
    #
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "         ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "*", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    # ░ ▒ ▓ █ ▄ ▀ ■ ▌▐
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 19, "▄░░░░▒░░▒▒░  ▓▒░▒░░▒░   ░    ░    ░▒▒░▒▒░▒", 0, True)
    #
    # Row 2
    #
    art.cd(0, 0, "      ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "              ", '', False)
    art.cd(255, 0, ".", '', False)
    # ░ ▒ ▓ █ ▄ ▀ ■ ▌▐
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 19, "▄ ░░▒▒░▒ ░░ ░░▒▒▒░▓░   ░  ░ ░░ ░▒░░░▒░░░", 0, True)

    #
    # Row 3
    #
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "      ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, "  ", '', False)

    art.cd(27, 0, "▀", '', False)
    art.cd(27, 19, "▄▄░▒░░░  ▒░  ░▒▒▒░▓░   ▒  ▒░  ▒ ░▒▓▒░░", 0, True)
    #
    # Row 4
    #
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 244, "▀▀█▀▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(255, 244, "▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█▀▀", '', False)
    art.cd(0, 0, "     ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "      ", '', False)
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 19, "▄▄░▒ ░░  ░   ░ ░▒░▒░  ░▓▒ ░▒▒░  ░ ░", 0, True)
    #
    # Row 5
    #
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, "█", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(255, 0, "█", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(255, 0, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(255, 0, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "█", '', False)
    art.cd(0, 0, "      ", '', False)
    art.cd(255, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)

    art.cd(27, 0, "▀", '', False)
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 19, "▄▄░░  ░ ░  ░ ░░▒░  ░ ▒ ░░ ░░ ▒░", 0, True)
    #
    # Row 6
    #
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 244, "█▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█▀▀█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "       ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "      ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 19, "▄▄▄░░ ░   ░░▒░░ ▒  ░   ░▒ ░", 0, True)

    #
    # Row 7
    #
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 254, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 254, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(255, 254, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 254, "█", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 254, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 254, "█", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 254, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 254, "█", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "       ", '', False)

    art.cd(27, 0, "▀", '', False)
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 0, "▀", '', False)
    art.cd(27, 19, "▄", '', False)
    art.cd(27, 19, "▄", '', False)
    art.cd(27, 19, "▄", '', False)
    art.cd(27, 19, "▄", '', False)
    art.cd(27, 19, "▄", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, "░", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, "░", '', False)
    art.cd(27, 19, "░", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, "░", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, "░", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, " ", '', False)
    art.cd(27, 19, "░", 0, True)

    #
    # Row 8
    #
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(255, 244, "█", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(255, 0, "▄▄", '', False)
    art.cd(255, 244, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(255, 0, "▄▄", '', False)
    art.cd(0, 0, "       ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 0, "*", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "     ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(27, 0, "▀▀▀▀▀", '', False)
    art.cd(27, 19, "▄▄▄▄▄▄▄▄▄▄", 0, True)
    #
    # Row 9
    #
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀▀▀", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "▀▀▀", '', False)
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "     ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "     ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "       ", 0, True)

    #
    # Row 10
    #
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(255, 244, "▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(255, 244, "▀▀▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(9, 1, "▀▀▀", '', False)
    art.cd(9, 0, "▄", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(9, 0, "▄", '', False)
    art.cd(9, 1, "▀▀", '', False)
    art.cd(9, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(9, 0, "▄", '', False)
    art.cd(9, 1, "▀▀", '', False)
    art.cd(9, 0, "▄", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(9, 1, "▀▀▀", '', False)
    art.cd(9, 0, "▄", '', False)
    art.cd(0, 0, "     ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "             ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", 0, True)  # star
    #
    # Row 11
    #
    art.cd(0, 0, "   ", '', False)
    art.cd(27, 0, "═══", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "══", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "════", '', False)
    art.cd(27, 0, "═══════", '', False)
    art.cd(19, 0, "══", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "══", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "══", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(19, 0, "══", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "══─", '', False)
    art.cd(19, 0, "──────────", '', False)
    art.cd(249, 0, "▐", '', False)
    art.cd(244, 0, "▌", '', False)
    art.cd(19, 0, "───────────", 0, True)
    #
    # Row 12
    #
    art.cd(0, 0, " ", '', False)
    art.cd(27, 0, "═════", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "══", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█▀▀█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(255, 244, "▀▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "══════", '', False)
    art.cd(9, 0, "▄", '', False)
    art.cd(9, 1, "▀▀", '', False)
    art.cd(1, 0, "▀", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(9, 0, "▄", '', False)
    art.cd(9, 1, "▀", '', False)
    art.cd(9, 1, "▀", '', False)
    art.cd(1, 0, "▀", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "════─", '', False)
    art.cd(19, 0, "────────", '', False)
    art.cd(249, 244, "█", '', False)
    art.cd(244, 244, "█", '', False)
    art.cd(19, 0, "───────────", 0, True)
    #
    # Row 13
    #
    art.cd(0, 0, "   ", '', False)
    art.cd(27, 0, "═══", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(19, 0, "══", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "══════", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "══", '', False)
    art.cd(27, 0, "══", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(27, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "═", '', False)
    art.cd(9, 1, "█", '', False)
    art.cd(19, 0, "══", '', False)
    art.cd(27, 0, "═════════─", '', False)
    art.cd(19, 0, "─────", '', False)
    art.cd(249, 244, "█", '', False)
    art.cd(244, 244, "█", '', False)
    art.cd(19, 0, "───────────", 0, True)
    #
    # Row 14
    #
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(255, 244, "▀", '', False)
    art.cd(255, 0, "▄", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 244, "█", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, "▄▄▄", '', False)
    art.cd(255, 244, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(9, 1, "▀▀▀▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(1, 0, "▀", '', False)
    art.cd(9, 1, "▀▀", '', False)
    art.cd(1, 0, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(1, 0, "▀", '', False)
    art.cd(9, 1, "▀▀", '', False)
    art.cd(1, 0, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(9, 1, "▀▀▀▀", '', False)
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "       ", '', False)
    art.cd(249, 244, "██▌", '', False)
    art.cd(244, 244, "█", '', False)
    art.cd(0, 0, "      ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", 0, True)
    #
    # Row 15
    #
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "▀▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀▀▀", '', False)
    art.cd(0, 0, "    ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "          ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "     ", '', False)
    art.cd(7, 0, "╒", '', False)
    art.cd(244, 249, "════", '', False)
    art.cd(244, 244, "  ", '', False)
    art.cd(244, 0, "╖", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "      ", 0, True)
    #
    # Row 16
    #
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "┌", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(244, 249, "─", '', False)
    art.cd(249, 244, "▄", '', False)
    art.cd(249, 244, "▄", '', False)
    art.cd(249, 244, "▄", '', False)
    art.cd(249, 244, "▄", '', False)
    art.cd(249, 244, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(249, 0, "▄", '', False)
    art.cd(0, 0, " ", 0, True)
    #
    # Row 17
    #
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "..", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "      ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "             ", '', False)
    art.cd(244, 0, "┌", '', False)
    art.cd(249, 0, "▄▄▄", '', False)
    art.cd(244, 249, "───────────────────────────", '', False)
    art.cd(249, 244, "▀▀▀▀▀▀▀▀▀▀", 0, True)
    #
    # Row 18
    #
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(249, 0, "▀", '', False)
    art.cd(255, 249, "──────────────────────────────", '', False)
    art.cd(249, 244, "▀", '', False)
    art.cd(244, 244, "██████████████", '', False)
    art.cd(244, 0, "▓", 0, True)
    #
    # Row 19
    #
    art.cd(0, 0, "   ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, "      ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(249, 0, "├", '', False)
    art.cd(255, 0, "─", '', False)
    art.cd(249, 0, "──┼", '', False)
    art.cd(255, 0, "─", '', False)
    art.cd(249, 0, "──┼", '', False)
    art.cd(255, 0, "─", '', False)
    art.cd(249, 0, "──┼─", '', False)
    art.cd(255, 0, "─", '', False)
    art.cd(249, 0, "─┼─", '', False)
    art.cd(255, 0, "─", '', False)
    art.cd(249, 0, "─┼─", '', False)
    art.cd(255, 0, "─", '', False)
    art.cd(249, 0, "─┼─", '', False)
    art.cd(255, 0, "─", '', False)
    art.cd(249, 0, "─┼─", '', False)
    art.cd(244, 0, "──┼───┼───┼───┼", '', False)
    art.cd(0, 0, " ", 0, True)
    #
    # Row 20
    #
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "  ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "         ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, "    ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, "   ", '', False)
    art.cd(249, 0, "▀", '', False)
    art.cd(249, 244, "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀", '', False)
    art.cd(244, 244, "████████████████", '', False)
    art.cd(244, 0, "▓", 0, True)
    #
    # Row 21
    #
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "▓", 0, True)
    #
    # Row 22
    #
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, "▀", '', False)
    art.cd(244, 0, ".", 0, True)  # star
    #
    # Row 23
    #
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "*", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(255, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, "╒", '', False)
    art.cd(244, 0, "▌", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "█", '', False)
    art.cd(244, 0, "▓", '', False)
    art.cd(244, 0, "▐", '', False)
    art.cd(244, 0, "╕", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", '', False)
    art.cd(244, 0, ".", '', False)  # star
    art.cd(0, 0, " ", '', False)
    art.cd(0, 0, " ", 0, True)
    art.cd(13, '', "[Pause]", 0, True)
    input("")


'''
    Characters from https://en.wikipedia.org/wiki/Code_page_437

    ░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
    · ∙ ° ° • . *

    ┌─┬─┐
    │ │ │
    ├─┼─┤
    └─┴─┘
'''
