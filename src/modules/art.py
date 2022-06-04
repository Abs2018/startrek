from colored import fg, bg, attr
'''
    Characters from https://en.wikipedia.org/wiki/Code_page_437

    ░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
    · ∙ ° ° • . * 
    ┌─┬─┐
    │ │ │
    ├─┼─┤
    └─┴─┘
    '''


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
