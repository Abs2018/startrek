# Import the required modules.
from modules import db
from modules import art

def createStarsTable(colour):
	# Create the Stars table
	#! Not sure if we need secid. See the 'Galaxy' table above.
	connection = db.stdb()
	query = """CREATE TABLE `stars` (
		`sid` int(128) NOT NULL,
		`secid` int(128),
		`x` int(128) NOT NULL,
		`y` int(128) NOT NULL,
		`starname` varchar(128),
		`scid` varchar(1) NOT NULL
		)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `stars` ADD PRIMARY KEY (`sid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `stars` MODIFY `sid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "Stellar matter formed.", "reset", True)