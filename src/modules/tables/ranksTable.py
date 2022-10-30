# Import the required modules.
from modules import db
from modules import art
from modules import func

def createRanksTable(colour):
	# Ranks table
	connection = db.stdb()
	query = """CREATE TABLE `ranks` (
		`rid` int(128) NOT NULL,
		`rankname` varchar(32) NOT NULL,
		`rankxp` int(16) NOT NULL,
		`empire` varchar(64) NOT NULL
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `ranks` ADD PRIMARY KEY (`rid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `ranks` MODIFY `rid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	query = "INSERT INTO `ranks` (`rankname`, `rankxp`, `empire`) VALUES (%s, %s, %s)"
	func.moduleload('ranks', query)

	art.cd(colour, '', "Organizing the rank and file.", "reset", True)
