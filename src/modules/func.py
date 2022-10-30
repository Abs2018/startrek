# General functions
import os
import platform
from csv import reader
from modules import db

# This will clear the screen.
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

# This module will read the CSV files in the data directory and import the values in them to their respective tables.
def moduleload(folder, query):
    # Get the path for the system
    opsys = (platform.system())     # Get the system type
    modpath = str(os.getcwd())      # Get the current working directory
    if opsys == "Windows":          # I believe Windows is the only OS that uses \
        slash = "\\"
    else:                           # All other OS's use /.
        slash = "/"
    modpath = modpath+slash+'data'+slash+folder+slash   # Create the directore path
    # print(modpath)
    # Define the list to be saved
    folderclass = []
    # Get the file listing in the folder variable and put it in a list
    for mod in os.listdir(modpath):
        # We will be avoiding the sample files that are provided as documentation examples.
        sample = modpath + '_Sample.txt'
        # Check if current mod is a file
        if os.path.isfile(os.path.join(modpath, mod)):
            # Avoid the sample file
            if os.path.join(modpath, mod) != sample:
                # Open each file and save its contents in a dictionary
                f = open(os.path.join(modpath, mod), "r", encoding="utf8")
                csv_reader = reader(f)
                for row in csv_reader:
                    folderclass.append(row)
                f.close()
    # print(folderclass)
    # Insert into database
    connection = db.stdb()
    db.querymany(connection, query, folderclass)

