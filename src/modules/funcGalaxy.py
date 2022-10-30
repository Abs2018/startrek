# This file has all the functions related to the galaxy.
# Import the required modules.
from modules import db

def galaxyradius():
    connection = db.stdb()
    query = "SELECT * FROM `settings` WHERE `settingname`='galaxyradius'"
    # print(query)
    results = db.query(connection, query)
    if results:
        for row in results:
            galaxyradius = int(row['settingvalue'])
    else:
        galaxyradius = "Unable to get the galaxy's radius."
    # print(type(galaxyradius))
    return galaxyradius