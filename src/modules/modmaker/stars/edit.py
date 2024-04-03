import csv
import os
import logging
from modules import art
from modules.menu import menufunc

LOG_FILE = 'logs/script_log.txt'


def setup_logging():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def get_star_classes(folder):
    star_classes = []

    try:
        for file_name in os.listdir(folder):
            if file_name.endswith(".csv"):
                star_class = os.path.splitext(file_name)[0]
                star_classes.append(star_class)
    except OSError as e:
        logging.error(f"Error: Failed to read star class folder: {e}")
        art.cd('red', '', "Error: Failed to read star class folder.", "reset", True)

    return star_classes

#! Can add validation here.


def validate_hex_color(color):
    # Add your validation logic here
    return True


def validate_shape(shape):
    # Add your validation logic here
    return True


def edit_star_class():
    star_classes_folder = 'data/starclass'
    star_classes = get_star_classes(star_classes_folder)

    if not star_classes:
        art.cd('red', '', "No star classes found.", "reset", True)
        return

    # Display a menu of star classes to choose from
    art.clear()
    menufunc.title("Edit Star Class")
    for index, star_class in enumerate(star_classes, start=1):
        menufunc.option(str(index), star_class)
    menufunc.quit("Back to Star Classes")
    menufunc.prompt("Enter the number of the star class to edit: ")

    # Get the user's choice
    choice = input("").strip()

    if choice.lower() == 'q':
        return

    if choice.isdigit() and 1 <= int(choice) <= len(star_classes):
        # Get the selected star class based on the index
        selected_star_class = star_classes[int(choice) - 1]
        file_path = os.path.join(
            star_classes_folder, f"{selected_star_class}.csv")
        sample_file_path = os.path.join(star_classes_folder, '_Sample.txt')

        try:
            with open(sample_file_path, 'r') as sample_file:
                headers = sample_file.readlines()[2].strip().split(',')

            with open(file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                rows = list(reader)

            if len(rows) < 1:
                art.cd('red', '', "Error: Star class CSV file is empty.",
                       "reset", True)
                return

            # Assuming the last row contains the current values
            current_values = rows[-1]

            # Create a dictionary to store the updated values
            updated_values = {}

            art.clear()
            menufunc.title(f"Edit Star Class: {selected_star_class}")

            for header, current_value in zip(headers, current_values):
                art.cd(5, '', f"Current {header.strip()}: ", '', False)
                art.cd('light_cyan', '', f"{current_value.strip()}", '', True)

                default_value = current_value if current_value != "" else "None"
                prompt = art.fg(
                    'green') + f"Enter new {header.strip()}" + art.fg(226) + f" (default: {default_value.strip()})" + art.fg('green') + f": " + art.attr('reset')
                value = input(prompt).strip()

                if header == "Star Class":
                    while True:
                        if value == "":
                            value = current_value
                        elif value in star_classes:
                            art.cd(
                                'red', '', f"Star Class {value} already exists. Please enter a new star class name:", "reset", True)
                            value = input("New Star Class Name: ").strip()
                            continue
                        break

                if header == "Colour":
                    # Validate the hex color value
                    if value == "":
                        value = current_value
                    elif not validate_hex_color(value):
                        art.cd(
                            'red', '', "Error: Invalid hex color. Please enter a valid hex color (e.g., #FFFFFF).", "reset", True)
                        continue

                if header == "Shape":
                    # Validate the shape value
                    if value == "":
                        value = current_value
                    elif not validate_shape(value):
                        art.cd(
                            'red', '', "Error: Invalid shape. Please enter either 'circle' or 'pulsar'.", "reset", True)
                        continue

                if len(value) < 1:
                    value = current_value

                updated_values[header] = value

            # Ask for the new star class name
            while True:
                new_star_class = input(
                    "Enter the new star class name: ").strip()

                # Check if the new star class name is blank
                if not new_star_class:
                    art.cd(
                        'red', '', "Error: Star class name cannot be blank.", "reset", True)
                    continue

                # Check if the new star class already exists
                new_file_path = os.path.join(
                    star_classes_folder, f"{new_star_class}.csv")
                if new_file_path != file_path and os.path.exists(new_file_path):
                    art.cd(
                        'red', '', f"Star Class {new_star_class} already exists. Please try again.", "reset", True)
                    continue

                break

            # Update the CSV file with the new values
            rows[-1] = [updated_values.get(header, "") for header in headers]

            if new_file_path != file_path:
                os.rename(file_path, new_file_path)

            with open(new_file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(rows)

            art.cd('green', '', "Star class updated successfully!", "reset", True)

            # Offer an option to return to the previous screen
            menufunc.quit("Return to Previous Screen")
            input("")

        except FileNotFoundError as e:
            logging.error(
                f"Error: Failed to open the sample or star class CSV file: {e}")
            art.cd(
                'red', '', "Error: Failed to open the sample or star class CSV file.", "reset", True)

    else:
        art.cd(
            'red', '', "Error: Invalid choice. Please enter a valid number.", "reset", True)


def main():
    setup_logging()
    edit_star_class()


if __name__ == "__main__":
    main()
