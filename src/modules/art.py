from colored import fg, bg, attr
import os
'''
    Characters from https://en.wikipedia.org/wiki/Code_page_437

    ░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
    · ∙ ° ° • . * 
    ┌─┬─┐
    │ │ │
    ├─┼─┤
    └─┴─┘
    '''
# define our clear function


def cd(fore, back, txt, attrib, newline):
    if fore == "":
        fore = ""
    else:
        fore = fg(fore)

    if back == "":
        back = ""
    else:
        back = bg(back)

    if attrib == "":
        attrib = ""
    else:
        attrib = attr(attrib)

    color = fore + back + txt + attrib

    if newline == True:
        print(color)
    else:
        print(color, end='')


def shipyards():
    print("")
    #
    # Row 1
    #
    cd(27, 0, '┌──────────────────────────────────┐                                            ', 0, True)
    #
    # Row 2
    #
    cd(27, 0, '│', '', False)
    cd(255, 0, '═╬═╬═╬═╬═╬═╬═╬', '', False)
    cd(196, 196, '█', '', False)
    cd(244, 0, ".  ", '', False)  # star
    cd(255, 0, ".", '', False)  # star
    cd(244, 0, ". ", '', False)  # star
    cd(255, 0, ". ", '', False)  # star
    cd(244, 0, ".  .", '', False)  # star
    cd(255, 0, " .  ", '', False)  # star
    cd(244, 0, " . ", '', False)  # star
    cd(27, 0, '│  ────────────────────────────────────────  ', 0, True)
    #
    # Row 3
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═╬═╬═╬═╬═╬═╬═╬', '', False)
    cd(1, 1, '█', '', False)
    cd(244, 0, " .  ", '', False)  # star
    cd(4, 0, ". ", '', False)  # star
    cd(244, 0, ".  ", '', False)  # star
    cd(255, 0, ".    ", '', False)  # star
    cd(244, 0, ".  ", '', False)  # star
    cd(244, 0, '│', '', False)
    cd(1, 0, ':', '', False)
    cd(27, 0, '│', '', False)
    cd(15, 0, '   As you enter the Federation Shipyards,   ', 0, True)

    #
    # Row 4
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═╬═╬═╬═╬═╬═╬═╬', '', False)
    cd(1, 1, '█', '', False)
    cd(244, 0, " .", '', False)  # star
    cd(255, 0, " .", '', False)  # star
    cd(244, 0, " .  .   ", '', False)  # star
    cd(255, 0, " .", '', False)  # star
    cd(244, 0, " . ", '', False)  # star
    cd(244, 0, '│', '', False)
    cd(255, 0, '│', '', False)
    cd(27, 0, '│', '', False)
    cd(15, 0, '   you pass by  row after  row of  ships.   ', 0, True)
    #
    # Row 5
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═', '', False)
    cd(12, 4, '│', '', False)
    cd(255, 4, 'Federation', '', False)
    cd(12, 4, '│', '', False)
    cd(244, 0, '╬', '', False)
    cd(1, 1, '█', '', False)
    cd(244, 0, " .    .   ", '', False)  # star
    cd(1, 0, ".", '', False)
    cd(255, 0, ". ", '', False)  # star
    cd(244, 0, ".", '', False)  # star
    cd(1, 0, ". ", '', False)
    cd(244, 0, '▐', '', False)
    cd(244, 7, '▀▀', '', False)
    cd(27, 0, '│', '', False)
    cd(15, 0, '   Most  of  them are  shiny and  new but   ', 0, True)
    #
    # Row 6
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═', '', False)
    cd(12, 4, '│', '', False)
    cd(255, 4, 'Shipyards', '', False)
    cd(27, 4, '.', '', False)
    cd(12, 4, '│', '', False)
    cd(244, 0, '╬', '', False)
    cd(1, 1, '█', '', False)
    cd(0, 0, '█', '', False)
    cd(244, 0, '▄', '', False)
    cd(7, 244, '▄▄▄', '', False)
    cd(7, 0, '▄', '', False)
    cd(7, 123, '▄▄', '', False)
    cd(7, 0, '▄─', '', False)
    cd(244, 0, '▐', '', False)
    cd(7, 0, '▄', '', False)
    cd(7, 123, '▄', '', False)
    cd(7, 0, '▄', '', False)
    cd(244, 0, '▌', '', False)
    cd(0, 0, ' ', '', False)
    cd(244, 0, '▐', '', False)
    cd(123, 7, '■', '', False)
    cd(0, 7, '█', '', False)
    cd(27, 0, '│', '', False)
    cd(15, 0, '   some show signs of use.  You recognize   ', 0, True)
    #
    # Row 7
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═', '', False)
    cd(12, 4, '│', '', False)
    cd(196, 4, '═══────═══', '', False)
    cd(12, 4, '│', '', False)
    cd(244, 0, '╬', '', False)
    cd(1, 1, '█', '', False)
    cd(4, 4, '██', '', False)
    cd(244, 4, '╜╜', '', False)
    cd(4, 4, '████', '', False)
    cd(244, 4, '└', '', False)
    cd(4, 4, '██', '', False)
    cd(244, 4, '┴┴┴', '', False)
    cd(4, 4, '█████', '', False)
    cd(27, 0, '│', '', False)
    cd(15, 0, '   the registrations on some of the older   ', 0, True)
    #
    # Row 8
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═╬═╬═╬═╬═╬═╬═╬', '', False)
    cd(1, 1, '█', '', False)
    cd(4, 0, '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓', '', False)
    cd(27, 0, '│', '', False)
    cd(15, 0, '   ships as craft you have seen  at other   ', 0, True)
    #
    # Row 9
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═╬═╬═╬═╬═╬═╬═╬', '', False)
    cd(1, 1, '█', '', False)
    cd(4, 0, '▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒', '', False)
    cd(27, 0, '│', '', False)
    cd(15, 0, '   trading ports before.                    ', 0, True)
    #
    # Row 10
    #
    cd(27, 0, '│', '', False)
    cd(244, 0, '═╬═╬═╬═╬═╬═╬═╬', '', False)
    cd(1, 1, '█', '', False)
    cd(4, 0, '░░░░░░░░░░░░░░░░░░░', '', False)
    cd(27, 0, '│', '', False)
    cd(27, 0, '  ────────────────────────────────────────  ', 0, True)
    #
    # Row 11
    #
    cd(27, 0, '└──────────────────────────────────┘                                            ', 0, True)


'''
    Characters from https://en.wikipedia.org/wiki/Code_page_437

    ░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
    · ∙ ° ° • . * 
    ┌─┬─┐
    │ │ │
    ├─┼─┤
    └─┴─┘
    '''


# 77x15
# Blue frame is 35
def portAnimClass0(portname):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Row 1
    cd(4, 0, "                                    ──────────────────────────────────────── ", 0, True)
    # Row 2
    cd(226, 0, "                                     You bring your ship into approach for   ", 0, True)
    # Row 3
    cd(4, 0, "┌─────────────────────────────────┐", 0, False)
    cd(226, 0, "  the Federation StarDock.                ", 0, True)
    # Row 4
    cd(4, 0, '│', '', False)
    cd(255, 0, '∙                         ', '', False)
    cd(7, 0, '∙  ', '', False)
    cd(15, 0, '∙   ', '', False)
    cd(4, 0, '│                                          ', 0, True)
    # Row 5
    cd(4, 0, '│  ', '', False)
    cd(7, 0, '∙        ', '', False)
    cd(255, 0, '∙', '', False)
    cd(7, 0, '∙  ', '', False)
    cd(9, 0, '▄ ', '', False)
    cd(7, 0, ' ∙           .  ', '', False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, 'This has to be the single, largest man- ', 0, True)
    # Row 6
    cd(4, 0, '│   ', '', False)
    cd(255, 0, '∙   ', '', False)
    cd(7, 0, '∙       ', '', False)
    cd(15, 0, '█ ', '', False)
    cd(7, 0, '      ∙    ', 0, False)
    cd(255, 0, '   . ', '', False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, "made object you've ever seen. It        ", 0, True)
    # Row 7
    cd(4, 0, '│       ', '', False)
    cd(15, 0, '═╕▄▄▄███', '', False)
    cd(7, 15, '▄▄██', '', False)
    cd(7, 0, '▄▄▄╒═  ∙  ', '', False)
    cd(226, 0, '∙   ', 0, False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, "continues for miles and contains the    ", 0, True)
    # Row 8
    cd(4, 0, '│ ', '', False)
    cd(7, 0, '∙  ', '', False)
    cd(255, 0, '∙     ', '', False)
    cd(15, 0, '▄▄▄▄', '', False)
    cd(7, 0, '▄▄▄▄▄▄▄', '', False)
    cd(7, 0, '    ∙', '', False)
    cd(255, 0, '∙      ', '', False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, "factories for all the major brands      ", 0, True)
    # Row 9
    cd(4, 0, '│', '', False)
    cd(7, 0, '      ∙      ', '', False)
    cd(0, 7, '▄', '', False)
    cd(7, 0, '███', '', False)
    cd(0, 7, '▄', '', False)
    cd(7, 0, '  ∙         .  ', '', False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, "of space-going craft. Since the         ", 0, True)
    # Row 10
    cd(4, 0, '│', '', False)
    cd(255, 0, '   ∙       .', '', False)
    cd(7, 0, ' . ', '', False)
    cd(7, 0, '█', '', False)
    cd(255, 0, '∙', '', False)
    cd(7, 0, '      .    .    ', '', False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, "materials wars of 1998 on Earth, all    ", 0, True)
    # Row 11
    cd(4, 0, '│', '', False)
    cd(7, 0, '   .    .      ', '', False)
    cd(7, 0, '█', '', False)
    cd(7, 0, '  ∙       .   .  ', '', False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, "ship builders relocated here. You've    ", 0, True)
    # Row 12
    cd(4, 0, '│', '', False)
    cd(226, 0, ' ∙', '', False)
    cd(7, 0, '   .       . ', '', False)
    cd(11, 7, '▄', '', False)
    cd(255, 0, '     ∙          .', '', False)
    cd(4, 0, '│  ', '', False)
    cd(14, 0, "heard many strange stories about the    ", 0, True)
    # Row 13
    cd(4, 0, "└─────────────────────────────────┘  ", 0, False)
    cd(14, 0, "people and places here, but you haven't ", 0, True)
    # Row 14
    cd(14, 0, "                                     found many of either, yet.              ", 0, True)
    # Row 15
    cd(4, 0, "                                    ──────────────────────────────────────── ", 0, True)
    cd(13, '', "[Pause]", 0, True)
    input("")
    os.system('cls' if os.name == 'nt' else 'clear')
    # Row 1
    cd(4, 0, "┌─────────────────────────────────┐", 0, False)
    cd(2, 0, " ──────────────────────────────────────── ", 0, True)
    # Row 2
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬╬╬╬     ', '', False)
    cd(1, 0, '.   .     .         ', '', False)
    cd(4, 0, '▒┼│  ', '', False)
    cd(15, 0, "You lose sight of the boundless reaches ", 0, True)
    # Row 3
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬╬╬╬', '', False)
    cd(1, 0, '.    ', '', False)
    cd(4, 0, '│   ░     │         ▒┼│  ', '', False)
    cd(15, 0, "of space as your craft descends amongst ", 0, True)
    # Row 4
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬╬╬╬', '', False)
    cd(4, 0, '│    ░   ░     ░        ▒┼┼│  ', '', False)
    cd(15, 0, "the giant buildings onto a landing pad. ", 0, True)
    # Row 5
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬╬', '', False)
    cd(4, 0, '╬╬░   ', '', False)
    cd(1, 0, '.', '', False)
    cd(4, 0, '░ ', '', False)
    cd(1, 0, '.', '', False)
    cd(4, 0, '░░  │  ░│      ▒', '', False)
    cd(12, 4, '┼', '', False)
    cd(4, 0, '┼┼│', '', False)
    cd(2, 0, " ──────────────────────────────────────── ", 0, True)
    # Row 6
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬╬', '', False)
    cd(4, 0, '╬╬░   ░░ ▒░░│ ░  ░░    ▒', '', False)
    cd(12, 4, '┼┼┼', '', False)
    cd(4, 0, '┼┼│    ┌─────────────────────────────────┐   ', 0, True)
    # Row 7
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬╬', '', False)
    cd(4, 0, '╬╬░  │░░ ▒░░░ ░  ░░   ▒▒', '', False)
    cd(12, 4, '┼┼┼', '', False)
    cd(4, 0, '┼┼│    │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░░░░░░░░░░░░░░░░░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 8
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬', '', False)
    cd(4, 0, '╬╬╬░', '', False)
    cd(1, 0, '. ', '', False)
    cd(4, 0, '░░░', '', False)
    cd(1, 0, '.', '', False)
    cd(4, 0, '▒░░░ ░', '', False)
    cd(1, 0, '. ', '', False)
    cd(4, 0, '░░', '', False)
    cd(1, 0, ' .', '', False)
    cd(4, 0, '░░░', '', False)
    cd(12, 4, '┼┼┼', '', False)
    cd(4, 0, '┼┼│    │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(15, 0, '█', 0, False)
    cd(15, 7, '▀▀▀▀▀▀▀▀▀▀▀▀▀', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 9
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬', '', False)
    cd(4, 0, '╬╬╬░', '', False)
    cd(7, 15, '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀', '', False)
    cd(4, 0, '░░░', '', False)
    cd(12, 4, '┼┼', '', False)
    cd(4, 0, '┼┼┼│    │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 7, '█', 0, False)
    cd(7, 15, '┌────═────┐', 0, False)
    cd(7, 7, '█', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 10
    cd(4, 0, '│▒▒', '', False)
    cd(12, 0, '╬', '', False)
    cd(4, 0, '╬╬╬░░', '', False)
    cd(15, 7, '▐', '', False)
    cd(0, 15, '▐', '', False)
    cd(4, 0, '░', '', False)
    cd(7, 0, '█', '', False)
    cd(4, 0, '░░░░░░░░', '', False)
    cd(7, 0, '█', '', False)
    cd(0, 7, '▐', '', False)
    cd(4, 0, '░', '', False)
    cd(15, 0, '█', '', False)
    cd(4, 0, '░░░░', '', False)
    cd(12, 4, '┼┼', '', False)
    cd(4, 0, '┼┼┼│    │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 7, '█', 0, False)
    cd(7, 15, '│┌   ', 0, False)
    cd(196, 15, '■', 0, False)
    cd(7, 15, '   ┐│', 0, False)
    cd(7, 7, '█', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 11
    cd(4, 0, "└─────────────────────────────────┘    │", 0, False)
    cd(7, 15, '┼┼┼┼┼┼', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 7, '█', 0, False)
    cd(7, 15, '║ ', 0, False)
    cd(196, 15, '■', 0, False)
    cd(7, 15, '  ┼  ', 0, False)
    cd(196, 15, '■', 0, False)
    cd(7, 15, ' ║', 0, False)
    cd(7, 7, '█', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 15, '┼┼┼┼┼┼', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 12
    cd(2, 0, " ──────────────────────────────────── ", 0, False)
    cd(4, 0, ' │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 7, '█', 0, False)
    cd(7, 15, '│└   ', 0, False)
    cd(196, 15, '■', 0, False)
    cd(7, 15, '   ┘│', 0, False)
    cd(7, 7, '█', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 13
    cd(7, 0, "  A message comes in on the intercom", '', False)
    cd(4, 0, '   │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 7, '█', 0, False)
    cd(7, 15, '└────═────┘', 0, False)
    cd(7, 7, '█', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 14
    cd(15, 0, '  \"', '', False)
    cd(1, 0, 'All systems secured, welcome to', '', False)
    cd(4, 0, '     │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '▀▀▀▀▀▀▀▀▀▀▀▀▀', 0, False)
    cd(15, 0, '█', 0, False)
    cd(7, 15, '░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 15
    spacelength = 34 - len(portname)
    spaces = ""
    i = 1
    while i < spacelength:
        spaces = spaces + " "
        i = i + 1
    cd(1, 0, '  ', '', False)
    cd(1, 0, portname, '', False)
    cd(15, 0, '\"', '', False)
    cd(15, 0, spaces, '', False)
    cd(4, 0, '   │', 0, False)
    cd(7, 0, '─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(1, 7, '▌', 0, False)
    cd(7, 0, '█', 0, False)
    cd(7, 15, '░░░░░░░░░░░░░░░░░', 0, False)
    cd(7, 0, '█', 0, False)
    cd(1, 7, '▐', 0, False)
    cd(7, 0, '─┼─', 0, False)
    cd(7, 15, '├┤', 0, False)
    cd(7, 0, '─', 0, False)
    cd(4, 0, '│   ', 0, True)
    # Row 16
    cd(2, 0, " ──────────────────────────────────── ", 0, False)
    cd(4, 0, " └─────────────────────────────────┘   ", 0, True)
