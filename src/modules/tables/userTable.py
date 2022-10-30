# Import the required modules.
from modules import db
from modules import art

def createUserTable(colour):
	# Create User Table
	connection = db.stdb()
	query = """CREATE TABLE `players` (
		`pid` int(24) NOT NULL,
		`callsign` varchar(128) NOT NULL,
		`fname` varchar(128) NOT NULL,
		`mname` varchar(128) NOT NULL,
		`lname` varchar(128) NOT NULL,
		`alignment` varchar(128) NOT NULL,
		`morality` varchar(16) NOT NULL,
		`rank` int(4) NOT NULL,
		`branch` varchar(16) NOT NULL,
		`xp` int(128) NOT NULL,
		`kills` int(128) NOT NULL,
		`deaths` int(128) NOT NULL,
		`locationx` int(24) NOT NULL,
		`locationy` int(24) NOT NULL,
		`whereami` varchar(24) NOT NULL,
		`health` int(24) NOT NULL,
		`species` varchar(24) NOT NULL,
		`age` int(24) NOT NULL,
		`birthday` varchar(24) NOT NULL,
		`homeplanet` varchar(24) NOT NULL,
		`languages` varchar(24) NOT NULL,
		`createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, 
		`lastlogin` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
		)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `players` ADD PRIMARY KEY (`pid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `players` MODIFY `pid` int(24) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "User Directory generated.", "reset", True)