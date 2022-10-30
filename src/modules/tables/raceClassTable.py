# Import the required modules.
from modules import db
from modules import art
from modules import func

def createRaceClassTable(colour):
	# Create the Race Class table
	connection = db.stdb()
	query = """CREATE TABLE `raceclass` (
		`rid` int(128) NOT NULL,
		`raceclass` varchar(128) NOT NULL,
		`description` varchar(4096),
		`strength` int(3) NOT NULL,
		`endurance` int(3) NOT NULL,
		`intellect` varchar(3) NOT NULL,
		`dexterity` varchar(3) NOT NULL,
		`charisma` varchar(3) NOT NULL,
		`luck` varchar(3) NOT NULL,
		`psionic` varchar(3) NOT NULL,
		`homeworld` varchar(128) NOT NULL,
		`empire` varchar(128) NOT NULL
		)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `raceclass` ADD PRIMARY KEY (`rid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `raceclass` MODIFY `rid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	query = "INSERT INTO `raceclass` (`raceclass`, `description`, `strength`, `endurance`, `intellect`, `dexterity`, `charisma`, `luck`, `psionic`, `homeworld`, `empire`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	func.moduleload('raceclass', query)

	art.cd(colour, '', "Evolving species.", "reset", True)
