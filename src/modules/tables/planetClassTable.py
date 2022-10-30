# Import the required modules.
from modules import db
from modules import func

def createPlanetClass():
	# Create Planet Class Table
	connection = db.stdb()
	query = """CREATE TABLE `planetclass` (
		`pcid` int(2) NOT NULL,
		`planetclass` varchar(1) NOT NULL,
		`Description` varchar(512) NOT NULL,
		`colour` varchar(7) NOT NULL
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `planetclass` ADD PRIMARY KEY (`pcid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `planetclass` MODIFY `pcid` int(2) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	query = "INSERT INTO `planetclass` (`planetclass`, `description`, `colour`) VALUES (%s, %s, %s)"
	func.moduleload('planetclass', query)
