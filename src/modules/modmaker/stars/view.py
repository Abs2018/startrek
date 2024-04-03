import csv
import os
import random
from modules import art
from modules import funcfile
from modules.menu import menufunc


def view_star_classes():
    directory_path = 'data/starclass'  # Path to the starclass directory
    # Retrieve the list of files in the directory
    files = funcfile.get_file_list(directory_path)
    menu_options = []  # Initialize an empty list for menu options

    # Generate menu options by removing ".csv" extension from each file name
    for file_name in files:
        menu_option = file_name[:-4]  # Remove the ".csv" extension
        menu_options.append(menu_option)  # Add the menu option to the list

    while True:
        art.clear()  # Clear the screen
        menufunc.title("Star Classes")  # Display the menu title

        # Display numbered menu options
        for index, option in enumerate(menu_options, start=1):
            menufunc.option(str(index), option)

        menufunc.quit("Back to Star Classes")  # Add the quit option to go back
        # Prompt the user for their choice
        menufunc.prompt("Enter your choice")
        # Read the user's choice as input and remove leading/trailing whitespace
        choice = input("").strip()

        # Handle the user's choice
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            # Get the selected option based on the index
            selected_option = menu_options[int(choice) - 1]
            # Call another function with the selected option
            open_star_item(directory_path, selected_option)
        elif choice.lower() == "q":
            break
        elif choice == "?":
            pass
        else:
            menufunc.error()  # Display an error message for an invalid choice


def open_star_item(directory_path, selected_option):
    # Read line 3 of _Sample.txt to get the header names
    sample_file_path = os.path.join(directory_path, '_Sample.txt')
    try:
        with open(sample_file_path, 'r') as sample_file:
            header_line = sample_file.readlines()[2].strip()
    except FileNotFoundError:
        print("Error: Failed to open _Sample.txt file.")
        return

    # Extract header names from the sample file line
    headers = [header.strip() for header in header_line.split(',')]

    # Store the headers and values from the selected CSV file in a dictionary
    selected_file_path = os.path.join(directory_path, selected_option + '.csv')
    csv_data = []
    try:
        with open(selected_file_path, 'r') as selected_file:
            csv_reader = csv.reader(selected_file)
            for row in csv_reader:
                item_data = {}
                for header, value in zip(headers, row):
                    item_data[header] = value
                csv_data.append(item_data)
    except FileNotFoundError:
        print(f"Error: Failed to open {selected_option}.csv file.")
        return

    # Display the headers and values from the dictionary
    art.clear()
    # print(csv_data)
    for item in csv_data:
        star_class = item['Star Class']
        star_colour = item['Colour']
        star_description = item['Description']
    show_star_info(star_class, star_colour, star_description)
    print_dictionary_info(csv_data)

    '''
    # To loop through all data:
    for item in csv_data:
        for header, value in item.items():
            print(f"{header}: {value}")
        print()
    # print(item[])

    # Access and print individual values using specific headers
    for item in csv_data:
        print(item['Star Class'])
        print(item['Colour'])
        print()
    '''

    # Offer an option to return to the previous screen
    menufunc.quit("Return to Previous Screen")
    input("")


def print_dictionary_info(dictionary_list):
    # Set the colors for key and value display
    key_color = "green"
    value_color = "light_cyan"

    # Check if the input is a list containing a dictionary
    if len(dictionary_list) != 1 or not isinstance(dictionary_list[0], dict):
        print("Invalid input format. Please provide a list containing a single dictionary.")
        return

    # Get the dictionary from the list
    dictionary = dictionary_list[0]

    # Get the keys and values from the dictionary, excluding the specified keys
    excluded_keys = ["Star Class", "Colour", "Shape", "Description"]
    keys = [key for key in dictionary.keys() if key not in excluded_keys]
    values = [dictionary[key] for key in keys]

    # Determine the maximum length of keys and values
    max_key_length = max(len(str(key)) for key in keys)
    max_value_length = max(len(str(value)) for value in values)

    # Calculate the number of columns
    num_columns = 2

    # Calculate the width of each column
    column_width = max_key_length + max_value_length + 4  # +4 for padding and colon

    # Iterate over the dictionary items and print them in columns
    for key, value in zip(keys, values):
        # Format the key and value with the specified colors
        formatted_key = art.fg(key_color) + str(key) + art.attr('reset') + \
            art.fg("yellow") + ":" + art.attr('reset')
        formatted_value = art.fg(value_color) + str(value) + art.attr('reset')

        # Print the formatted key-value pairs with appropriate padding
        print("{:<{width}} {:<{width}}".format(
            formatted_key, formatted_value, width=column_width))

    print()  # Move to the next line


def show_star_info(classname, colour, description):
    # Outline colour
    outline_colour = art.increase_hex_color(colour, 30)
    # Glow colour
    glow = art.decrease_hex_color(colour, 60)
    # Sunspot randomness percentage
    sun_spot_randomness = 30
    # Title string for centering
    titlestring = "Star Class Type "+str(classname)
    left_spaces, right_spaces = art.title_center(titlestring, 56)
    # Description formatting
    descspacing = "      "
    desc1, desc2, desc3, desc4, desc5 = cut_description(description)

    # Line 1
    art.cd("red", "black", "  ┌──────────────────┐  ", "", False)
    art.cd("white", "black", left_spaces+"Star Class Type ", "", False)
    art.cd(colour, "", str(classname)+right_spaces, "", True)
    # Line 2
    art.cd("red", "black", "  │       ", "", False)
    art.cd(glow, "black", "▄▄▄▄", "", False)
    art.cd("red", "black", "       │", "", False)
    art.cd("blue", "black",
           "    ──────────────────────────────────────────────────    ", "", True)
    # Line 3
    art.cd("red", "black", "  │    ", "", False)
    art.cd(glow, "black", "▄", "", False)
    art.cd(outline_colour, glow, "▄▄", "", False)
    art.cd(outline_colour, colour, "▀▀▀▀", "", False)
    art.cd(outline_colour, glow, "▄▄", "", False)
    art.cd(glow, "black", "▄", "", False)
    art.cd("red", "black", "    │", "", False)
    art.cd("white", "black", descspacing+desc1+descspacing, "", True)
    # Line 4
    art.cd("red", "black", "  │   ", "", False)
    art.cd("white", glow, " ", "", False)
    art.cd(outline_colour, colour, "█", "reset", False)
    i = 1
    while i < 9:
        character, adjusted_colour = random_sun_spots(
            colour, sun_spot_randomness)
        if character == ' ':
            art.cd("white", colour, " ", "reset", False)
        else:
            art.cd(adjusted_colour, colour, character, "reset", False)
        i += 1
    art.cd(outline_colour, colour, "█", "", False)
    art.cd("white", glow, " ", "", False)
    art.cd("red", "black", "   │", "", False)
    art.cd("white", "black", descspacing+desc2+descspacing, "", True)
    # Line 5
    art.cd("red", "black", "  │  ", "", False)
    art.cd("white", glow, " ", "", False)
    art.cd(outline_colour, colour, "█", "", False)
    i = 1
    while i < 11:
        character, adjusted_colour = random_sun_spots(
            colour, sun_spot_randomness)
        if character == ' ':
            art.cd("white", colour, " ", "reset", False)
        else:
            art.cd(adjusted_colour, colour, character, "reset", False)
        i += 1
    art.cd(outline_colour, colour, "█", "", False)
    art.cd("white", glow, " ", "", False)
    art.cd("red", "black", "  │", "", False)
    art.cd("white", "black", descspacing+desc3+descspacing, "", True)
    # Line 6
    art.cd("red", "black", "  │   ", "", False)
    art.cd("white", glow, " ", "", False)
    art.cd(outline_colour, colour, "█", "reset", False)
    i = 1
    while i < 9:
        character, adjusted_colour = random_sun_spots(
            colour, sun_spot_randomness)
        if character == ' ':
            art.cd("white", colour, " ", "reset", False)
        else:
            art.cd(adjusted_colour, colour, character, "reset", False)
        i += 1
    art.cd(outline_colour, colour, "█", "", False)
    art.cd("white", glow, " ", "", False)
    art.cd("red", "black", "   │", "", False)
    art.cd("white", "black", descspacing+desc4+descspacing, "", True)
    # Line 7
    art.cd("red", "black", "  │    ", "", False)
    art.cd(glow, "black", "▀", "", False)
    art.cd(outline_colour, glow, "▀▀", "", False)
    art.cd(outline_colour, colour, "▄▄▄▄", "", False)
    art.cd(outline_colour, glow, "▀▀", "", False)
    art.cd(glow, "black", "▀", "", False)
    art.cd("red", "black", "    │", "", False)
    art.cd("white", "black", descspacing+desc5+descspacing, "", True)
    # Line 8
    art.cd("red", "black", "  │       ", "", False)
    art.cd(glow, "black", "▀▀▀▀", "", False)
    art.cd("red", "black", "       │", "", False)
    art.cd("blue", "black",
           "    ──────────────────────────────────────────────────    ", "", True)
    # Line 9
    art.cd("red", "black", "  └──────────────────┘", "reset", True)


def cut_description(description):
    if len(description) <= 46:
        # If the description is already short enough, fill the remaining variables with spaces
        remaining_spaces = 5 - len(description)
        return (description.strip(),) + ("",) * remaining_spaces + ("",) + ("",) + ("",) + ("",)
    else:
        # Cut the description into pieces of 46 characters each
        chunks = [description[i:i+46].strip()
                  for i in range(0, len(description), 46)]

        # Fill the remaining variables with spaces if needed
        chunks.extend([""] * (5 - len(chunks)))

        # Return the five variables
        return tuple(chunks[:5])


def random_sun_spots(colour, sun_spot_randomness):
    # Generate a random number between 0 and 99
    random_number = random.randint(0, 99)

    if random_number < sun_spot_randomness:
        # 75% chance of returning a blank space
        return ' ', None
    else:
        # 25% chance of returning a character and modified color
        characters = ['░', '▒', '▓']
        selected_character = random.choice(characters)
        increase_amount = random.randint(
            0, 5) * 5  # Increase amount in increments of 5%

        # Increase or decrease the color intensity based on the randomly chosen character
        if selected_character == '░':
            adjusted_colour = art.increase_hex_color(colour, increase_amount)
        else:
            adjusted_colour = art.decrease_hex_color(colour, increase_amount)

        return selected_character, adjusted_colour


'''
    ░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌	· ∙ ° ° • . * 
'''
