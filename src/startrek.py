# This is the game controller script.

# Import the required modules.
import mysql.connector
from mysql.connector import Error
from classes import playerClass
from classes import log
from classes import menus
from modules import db
from modules import art
from classes import intro

# Check to see if the 'startrek' database exists.
connection = db.stdb()
if connection == "FALSE":
    art.cd(5, '', "Unable to communicate with ", "", False)
    art.cd(15, 4, "Starfleet Command", "reset", False)
    art.cd(5, '', ". Please run ", "", False)
    art.cd(226, '', "python admin.py ", "", False)
    art.cd(5, '', "to set up the game first.", "reset", True)
    quit()
# Also need to check if the galaxy has been created.


# Show a random intro screen.
# print("Hello world!")
intro.mainscreen()
player = playerClass.player()
player.playerCheck()