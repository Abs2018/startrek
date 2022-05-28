import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


class player():
    def __init__(self):
        pass

    def playerCheck(self):
        # Get the player name.
        art.cd(13, '', "", '', False)
        playername = input("What is your name? ")
        art.cd(4, '', "", 0, False)
        # Check the DB for player.
        connection = db.stdb()
        query = "select * from `players` where `name` = '"+playername+"'"
        results = db.rowcount(connection, query)
        if results == 0:
            # Register player
            print("We need your name.")
        else:
            # Load player information
            print("We found you.")
