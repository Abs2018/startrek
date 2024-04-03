import os
import csv
import re
from modules import art
from modules.menu import menufunc


def create_star_class():
    sample_file_path = os.path.join('data/starclass', '_Sample.txt')

    try:
        with open(sample_file_path, 'r') as sample_file:
            header_line = sample_file.readlines()[2].strip()
    except FileNotFoundError:
        print("Error: Failed to open _Sample.txt file.")
        return

    # Extract header names from the sample file line
    headers = [header.strip() for header in header_line.split(',')]

    # Create a dictionary to store the user's input values
    user_input = {}

    # Prompt the user for input values for each header
    for header in headers:
        while True:
            value = input(f"Enter {header}: ").strip()

            if header == "Star Class":
                # Convert "Star Class" to uppercase
                value = value.upper()

            if header == "Colour":
                # Check if "Colour" is a valid hex color
                if not re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):
                    art.cd(
                        'red', '', "Error: Invalid hex color. Please enter a valid hex color (e.g., #FFFFFF).", "reset", True)
                    continue

            if header == "Shape":
                # Check if "Shape" is either "circle" or "pulsar"
                if value.lower() not in ["circle", "pulsar"]:
                    art.cd(
                        'red', '', "Error: Invalid shape. Please enter either 'circle' or 'pulsar'.", "reset", True)
                    continue

            if header in ["Temperature (Kelvin)", "Mass", "Radius", "Luminosity"]:
                # Check if the value is a valid range
                if not re.match(r'^\d+(?:\.\d+)?-\d+(?:\.\d+)?$', value):
                    art.cd(
                        'red', '', "Error: Invalid range. Please enter a valid range (e.g., 100-200 or 1.5-2.5).", "reset", True)
                    continue

            if len(value) < 1:
                art.cd(
                    'red', '', "Error: Value must be at least 1 character long.", "reset", True)
            else:
                user_input[header] = value
                break

    # Create a new CSV file with the user's input values
    star_class_name = user_input['Star Class']
    file_path = os.path.join('data/starclass', f"{star_class_name}.csv")

    try:
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Write the user's input values
            writer.writerow([user_input.get(header, "") for header in headers])
    except IOError:
        art.cd(
            'red', '', "Error: Failed to create the star class CSV file.", "reset", True)
        return

    print("Star class created successfully!")

    # Offer an option to return to the previous screen
    menufunc.quit("Return to Previous Screen")
    input("")
