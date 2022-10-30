# This file has all the functions related to ships.
# Import the required modules.
from modules import db

def anyships():
    connection = db.stdb()
    query = "SELECT * FROM `ships`"
    # print(query)
    results = db.query(connection, query)
    if results:
        shipcount = len(results)
    else:
        shipcount = "No ships found."
    return shipcount