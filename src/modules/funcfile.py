import os


# Put this in a separate gamefiles module.


def get_file_list(directory_path):
    current_directory = os.path.abspath(os.path.join(os.getcwd()))
    full_path = os.path.join(current_directory, *directory_path.split("/"))
    file_list = os.listdir(full_path)
    file_list = [
        file_name for file_name in file_list if file_name != '_Sample.txt']
    return file_list
