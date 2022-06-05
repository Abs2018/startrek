# This is the game controller script.

# Import the required modules.
from classes import port
from classes import player
from classes import ship
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
command = ""
# Instantiate Player Ship
shipinfo = ship.ship(playerinfo.pid)
command = ""

while True:
    match command:
        case 'q':  # Quit the whole game.
            print("")
            art.cd(255, 4, "Live long and prosper.", 0, True)
            print("")
            quit()
        case _:
            if playerinfo.whereami == "port":
                # Get the dock information using the location.
                portinfo = port.port(
                    playerinfo.locationx, playerinfo.locationy)
                # print(portinfo.portname)
                menu.portmenu(portinfo, playerinfo)

                # if playerinfo.locationx == 0 and playerinfo.locationy == 0:
                #     menu.spacedock(playerinfo)
                # else:
                #     pass
            elif playerinfo.whereami == "ship":
                # m.playership(path, slash, player)
                menu.shipmenu(shipinfo, playerinfo)
            elif playerinfo.whereami == "planet":
                pass
