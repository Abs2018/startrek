# Import the required modules.
from modules import db
from modules import art

def createPlanetsTable(colour):
	# Create the Planets table
	#! Not sure if we need secid. See the 'Galaxy' table above.
	connection = db.stdb()
	query = """CREATE TABLE `planets` (
		`pid` int(128) NOT NULL,
		`secid` int(128),
		`x` int(128) NOT NULL,
		`y` int(128) NOT NULL,
		`sid` int(128), `planetname`
		varchar(128),
		`pcid` varchar(2) NOT NULL,
		`cid` varchar(128) NOT NULL DEFAULT '0'
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `planets` ADD PRIMARY KEY (`pid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `planets` MODIFY `pid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "Aligning planet orbits.", "reset", True)