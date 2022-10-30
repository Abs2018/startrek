# Import the required modules.
from modules import db
from modules import art

def createLogsTable(colour):
	# Create the Logs table
	connection = db.stdb()
	query = """CREATE TABLE `logs` (
		`lid` int(128) NOT NULL,
		`logtype` varchar(24),
		`log` varchar(128) NOT NULL,
		`createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
		)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `logs` ADD PRIMARY KEY (`lid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `logs` MODIFY `lid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "Starting the historic record.", "reset", True)
