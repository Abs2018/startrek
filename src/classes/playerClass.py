import mysql.connector
from mysql.connector import Error
from modules import db

class player():
	def __init__(self):
		pass
	def playerCheck(self):
		# Get the player name.
		playername = input("What is your name? ")
		# Check the DB for player.
		connection = db.stdb()
		query = "select * from `players` where `name` = '"+playername+"'"
		results = db.rowcount(connection, query)
		if results == 0:
			# Register player
			print("We need your name.")
		else :
			# Load player information
			print("We found you.")
