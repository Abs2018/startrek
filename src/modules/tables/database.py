# Import the required modules.
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art

def createDatabase(colour):
    # Since there is no database, we have to create a connection to only the server, hence we are not using the db function.
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        # print("Connection to MySQL DB successful")
    except Error as e:
        # print(f"The error '{e}' occurred")
        connection = "FALSE"
    # Create the database.
    query = "CREATE DATABASE IF NOT EXISTS `startrek`"
    db.query(connection, query)
    art.cd(colour, '', "Game database created.", "reset", True)
    