# This is the admin app.

# Import the required modules.
#import mysql.connector
#from mysql.connector import Error
import os
from modules import func
from modules import db
from modules import art
from modules import setup
from modules.menu.adm import main



connection = db.stdb()
if connection == "FALSE":
	func.clear()
	# The database has not been installed. Display setup menu.
	art.cd(22, '', "First time setup detected.", "reset", True)
	setup.setup()


main.menu()