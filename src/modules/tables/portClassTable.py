# Import the required modules.
from modules import db
from modules import func

def createPortClass():
	# Create Port Classes Table
	'''
	Port classes are a function of size, not what they trade in.
	The first 3 classes (0,1,2) will offer shipyard services, the number of services reducing the lower the class goes.

	'''
	connection = db.stdb()
	query = """CREATE TABLE `portclass` (
		`pcid` int(8) NOT NULL,
		`portclass` varchar(8) NOT NULL,
		`orecap` varchar(7) NOT NULL,
		`organicscap` varchar(7) NOT NULL,
		`equipmentcap` varchar(7) NOT NULL,
		`theater` int(1) NOT NULL,
		`bank` int(1) NOT NULL,
		`techdealer` int(1) NOT NULL,
		`police` int(1) NOT NULL,
		`shipyards` int(1) NOT NULL,
		`tavern` int(1) NOT NULL,
		`library` int(1) NOT NULL,
		`blackmarket` int(1) NOT NULL,
		`bar` int(1) NOT NULL,
		`description` varchar(1024) NOT NULL
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `portclass` ADD PRIMARY KEY (`pcid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `portclass` MODIFY `pcid` int(8) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	'''
	class, orecap, organicscap, equipmentcap, theater, bank, techdealer, police, shipyards, bar, library, blackmarket
	'''
	query = "INSERT INTO `portclass` (`portclass`, `orecap`, `organicscap`, `equipmentcap`, `theater`, `bank`, `techdealer`, `police`, `shipyards`, `tavern`, `library`, `blackmarket`, `bar`, `description`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	func.moduleload('portclass', query)
