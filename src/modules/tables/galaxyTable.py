# Import the required modules.
from modules import db
from modules import art

def createGalaxyTable(colour):
	# ? Is this table needed, or can we just store the sector coordinates with the stars and planets?
	#! .....................UP FOR REVIEW.....................
	# Create Galaxy Table
	connection = db.stdb()
	query = "CREATE TABLE `galaxy` (`secid` int(128) NOT NULL, `x` int(128) NOT NULL, `y` int(128) NOT NULL, `name` int(128))"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `galaxy` ADD PRIMARY KEY (`secid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `galaxy` MODIFY `secid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "Galactic Fabric woven.", "reset", True)