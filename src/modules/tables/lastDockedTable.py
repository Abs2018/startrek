# Import the required modules.
from modules import db
from modules import art

def createLastDockedTable(colour):
	# Last Time Docked
	connection = db.stdb()
	query = """CREATE TABLE `portlastdocked` (
		`ldapid` int(128) NOT NULL,
		`portid` int(8),
		`pid` int(8) NOT NULL,
		`lastdockeddate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `portlastdocked` ADD PRIMARY KEY (`ldapid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `portlastdocked` MODIFY `ldapid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "Placing safe harbours throughout the galaxy.", "reset", True)
