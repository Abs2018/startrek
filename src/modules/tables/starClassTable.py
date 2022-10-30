# Import the required modules.
from modules import db
from modules import func

# This funtion creates the starclass table, and then imports the class types from the data\starclass folder. 
def createStarClassTable():
	# Create Star Class Table
	connection = db.stdb()
	query = """CREATE TABLE `starclass` (
		`scid` int(2) NOT NULL,
		`starclass` varchar(1) NOT NULL,
		`colour` varchar(7) NOT NULL
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `starclass` ADD PRIMARY KEY (`scid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `starclass` MODIFY `scid` int(2) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	connection = db.stdb()
	query = "INSERT INTO `starclass` (`starclass`, `colour`) VALUES (%s, %s)"
	func.moduleload('starclass', query)
