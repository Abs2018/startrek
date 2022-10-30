# This file has all the functions related to players.
# Import the required modules.
from modules import db

def anyplayers():
    connection = db.stdb()
    query = "SELECT * FROM `players`"
    # print(query)
    results = db.query(connection, query)
    if results:
        playercount = len(results)
    else:
        playercount = "No players found."
    return playercount