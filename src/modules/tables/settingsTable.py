# Import the required modules.
from modules import db
from modules import art

def createSettingsTable(colour):
	# Create Settings Table.
	# This table stores information such as:
	# Total sectors
	# Height/Width of Galaxy, etc
	connection = db.stdb()
	query = """CREATE TABLE `settings` (
		`sid` int(24) NOT NULL,
		`settingname` varchar(128) NOT NULL,
		`settingvalue` varchar(128) NOT NULL,
		`createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
		)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `settings` ADD PRIMARY KEY (`sid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `settings` MODIFY `sid` int(24) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "Game Settings prepared.", "reset", True)