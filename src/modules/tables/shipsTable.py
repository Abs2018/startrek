# Import the required modules.
from modules import db
from modules import art

def createShipsTable(colour):
	# Ships table
	connection = db.stdb()
	query = """CREATE TABLE `ships` (
		`shid` int(128) NOT NULL,
		`shipname` varchar(32) NOT NULL,
		`ownedby` int(16) NOT NULL,
		`active` int(16) NOT NULL,
		`ports` int(16) NOT NULL,
		`kills` int(16),
		`shipclass` int(128),
		`cloaked` int(1) NOT NULL,
		`locationx` int(128) NOT NULL,
		`locationy` int(128) NOT NULL,
		`fighters` int(16) NOT NULL,
		`shields` int(8) NOT NULL,
		`holds` int(8) NOT NULL,
		`invfuelore` int(8) NOT NULL,
		`invorganics` int(8) NOT NULL,
		`invequipment` int(8) NOT NULL,
		`invcolonists` int(8) NOT NULL,
		`genesistorpedoes` int(8) NOT NULL,
		`mines` int(8) NOT NULL,
		`markerbeacons` int(8) NOT NULL,
		`holoscanner` int(1) NOT NULL,
		`transwarpdrive` int(1) NOT NULL,
		`onplanetnum` int(16) NOT NULL,
		`cloakingdevices` int(8) NOT NULL,
		`interdicting` int(1) NOT NULL,
		`atomicdetonators` int(8) NOT NULL,
		`corbomitedevices` int(8) NOT NULL,
		`subspaceetherprobes` int(8) NOT NULL,
		`minedisruptors` int(8) NOT NULL,
		`photontorpedoes` int(8) NOT NULL,
		`psychicprobe` int(1) NOT NULL,
		`planetscanner` int(1) NOT NULL
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `ships` ADD PRIMARY KEY (`shid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `ships` MODIFY `shid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	art.cd(colour, '', "Finalizing ship blueprints.", "reset", True)