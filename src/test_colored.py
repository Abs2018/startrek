from colored import fg, bg, attr


def spacing(i):
    if i < 10:
        space = "       "
    elif i >= 10 and i < 100:
        space = "      "
    else:
        space = "     "
    return space


print("\nColored Text:")

j = 1
for i in range(0, 256):
    color = fg(i)

    if j != 10:
        print(color+str(i)+"\t", end='')
        j = j+1
    else:
        print(color+str(i)+"\t")
        j = 1

print(attr("reset"))

print("\nColored Background:")

j = 1
for i in range(0, 256):
    color = bg(i)+fg('white')

    space = spacing(i)

    if j != 10:
        print(color+str(i)+space, end='')
        j = j+1
    else:
        print(color+str(i)+space+attr("reset"))
        j = 1

print(attr("reset"))

print("\nColored Attributes:")
'''
+-----+------------------+
|Code | Description      |
+-----+------------------+
|  1  | bold             |
|  2  | dim              |
|  4  | underlined       |
|  5  | blink            |
|  7  | reverse          |
|  8  | hidden           |
|  0  | reset            |
|  21 | res_bold         |
|  22 | res_dim          |
|  24 | res_underlined   |
|  25 | res_blink        |
|  27 | res_reverse      |
|  28 | res_hidden       |
+------------------------+
'''
coloredattribs = [1, 2, 4, 5, 7, 8, 0, 21, 22, 24, 25, 27, 28]
for i in coloredattribs:
    color = fg(196)
    attrib = attr(i)

    print(color+"Attribute"+attrib)

print(attr("reset"))
