from colored import fg, bg, attr


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
