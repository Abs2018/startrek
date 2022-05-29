# This is the game controller script.

# Import the required modules.
from classes import player
from classes import log
from classes import intro
from modules import art
from modules import db
from classes import menus
import mysql.connector
from mysql.connector import Error
from classes import playerClass
playerClass = playerClass.player()
log = log.log()
menu = menus.menus()

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
intro.mainscreen()
# Show the starting menu (high scores, etc)
menu.gameStart()
# Check to see if the player is in the database. If so, save the callsign and instantiate the player.
pid = playerClass.check()
log.logShow()
# Instantiate Player
playerinfo = player.player(pid)
# print("Hello Cadet "+str(playerinfo.lname))
