import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art

class highScores():
	def __init__(self):
		pass
	
	def show(self):
		# Check the DB for player.
		connection = db.stdb()
		query = "select * from `highscores`"
		results = db.rowcount(connection, query)
		if results == 0:
			# Register player
			print("")
			print("High Score Table is empty.")
			print("")
		else:
			# Load player information
			print("")
			print("There are high scores available!")
			print("")
