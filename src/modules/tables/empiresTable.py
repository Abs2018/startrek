# Import the required modules.
from modules import db
from modules import art
from modules import func

def createEmpiresTable(colour):
	# Create the Empires table
	#! Need to add other columns here, like foreground colour, bg colour, resources,/score, etc.
	#* X and Y can be the coordinates that the empire starts at, and then expands based on economic power.
	connection = db.stdb()
	query = """CREATE TABLE `empires` (
		`eid` int(128) NOT NULL,
		`secid` int(128),
		`x` int(128) NOT NULL,
		`y` int(128) NOT NULL,
		`empname` varchar(128),
		`spaceforce` varchar(128)
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `empires` ADD PRIMARY KEY (`eid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `empires` MODIFY `eid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	query = "INSERT INTO `empires` (`x`, `y`, `empname`, `spaceforce`) VALUES (%s, %s, %s, %s)"
	func.moduleload('empires', query)

	art.cd(colour, '', "Creating the conditions for life.", "reset", True)
