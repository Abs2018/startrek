# This file has all the functions related to Empires.
# Import the required modules.
from modules import db

def anyempires():
    connection = db.stdb()
    query = "SELECT * FROM `empires`"
    # print(query)
    results = db.query(connection, query)
    if results:
        empirecount = len(results)
    else:
        empirecount = "No empires found."
    return empirecount