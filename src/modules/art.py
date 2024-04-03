from colored import fg, bg, attr
import os


# This will clear the screen.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Custom function to display colours in console.
def cd(fore, back, txt, attrib, newline):
    if fore == "":
        fore = ""
    else:
        fore = fg(fore)

    if back == "":
        back = ""
    else:
        back = bg(back)
        # Most likely attribute you want it "reset", all lowercase.
    if attrib == "":
        attrib = ""
    else:
        attrib = attr(attrib)

    color = fore + back + txt + attrib

    if newline == True:
        print(color)
    else:
        print(color, end='')

# Decrease the intensity of a colour


def decrease_hex_color(hex_color, reduction_amount):
    # Remove the '#' symbol and extract the RGB values
    hex_color = hex_color.strip('#')
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    # Calculate the reduction factor based on the reduction amount
    reduction_factor = 1 - (reduction_amount / 100)

    # Reduce the RGB values by the reduction factor
    red = int(red * reduction_factor)
    green = int(green * reduction_factor)
    blue = int(blue * reduction_factor)

    # Ensure the values stay within the valid range (0-255)
    red = max(red, 0)
    green = max(green, 0)
    blue = max(blue, 0)
    red = min(red, 255)
    green = min(green, 255)
    blue = min(blue, 255)

    # Convert the adjusted RGB values back to hexadecimal
    adjusted_hex_color = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    return adjusted_hex_color


# Increase the intensite of a colour
def increase_hex_color(hex_color, increase_amount):
    # Remove the '#' symbol and extract the RGB values
    hex_color = hex_color.strip('#')
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    # Calculate the increase factor based on the increase amount
    increase_factor = 1 + (increase_amount / 100)

    # Increase the RGB values by the increase factor
    red = int(min(red * increase_factor, 255))
    green = int(min(green * increase_factor, 255))
    blue = int(min(blue * increase_factor, 255))

    # Convert the adjusted RGB values back to hexadecimal
    adjusted_hex_color = "#{:02x}{:02x}{:02x}".format(red, green, blue)

    return adjusted_hex_color

# Returns the spaces on either side of a title. Doesn't return the title to
# allow for colour customization.


def title_center(title, ui_element_width):
    title_length = len(title)
    remaining_space = ui_element_width - title_length

    left_spaces = ' ' * (remaining_space // 2)
    right_spaces = ' ' * (remaining_space - len(left_spaces))

    return left_spaces, right_spaces
