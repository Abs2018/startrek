# Import the required modules.
from modules import db
from modules import art

def createHighScoresTable(colour):
	# Create High Scores Table
	connection = db.stdb()
	query = """CREATE TABLE `highscores` (
		`hsid` int(2) NOT NULL,
		`pid` int(9) NOT NULL,
		`score` int(64) NOT NULL,
		`createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
		)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `highscores` ADD PRIMARY KEY (`hsid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `highscores` MODIFY `hsid` int(2) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "High Scores Board built.", "reset", True)
