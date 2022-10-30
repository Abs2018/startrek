# Import the required modules.
from modules import db

def createPortsTable():
	# Create the Ports table
	connection = db.stdb()
	query = """CREATE TABLE `ports` (
		`portid` int(128) NOT NULL,
		`portclass` int(8) NOT NULL,
		`portname` varchar(128) NOT NULL,
		`locationx` int(16) NOT NULL,
		`locationy` int(16) NOT NULL,
		`orecount` INT(5) NOT NULL,
		`organicscount` INT(5) NOT NULL,
		`equipmentcount` INT(5) NOT NULL,
		`createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `ports` ADD PRIMARY KEY (`portid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `ports` MODIFY `portid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)
