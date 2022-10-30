# Import the required modules.
from modules import db
from modules import func

def createShipClassTable():
	# Ship Class table
	connection = db.stdb()
	query = """CREATE TABLE `shipclass` (
		`shcid` int(128) NOT NULL,
		`shipclassname` varchar(32) NOT NULL,
		`fgcolour` int(7) NOT NULL,
		`bgcolour` int(7) NOT NULL,
		`alignment` varchar(24),
		`manufacturer` varchar(48),
		`cargoholdsstart` int(8) NOT NULL,
		`cargoholdsmax` int(8) NOT NULL,
		`fightersstart` int(8) NOT NULL,
		`fightersmax` int(8) NOT NULL,
		`fighterattackforce` int(8) NOT NULL,
		`photontorpedoesstart` int(8) NOT NULL,
		`photontorpedoesmax` int(8) NOT NULL,
		`shieldsstart` int(8) NOT NULL,
		`shieldsmax` int(8) NOT NULL,
		`minesstart` int(8) NOT NULL,
		`minesmax` int(8) NOT NULL,
		`minedisruptorsstart` int(8) NOT NULL,
		`minedisruptorsmax` int(8) NOT NULL,
		`markerbeaconsstart` int(8) NOT NULL,
		`markerbeaconsmax` int(8) NOT NULL,
		`genesistorpedoes` int(8) NOT NULL,
		`cloakingdevices` int(8) NOT NULL,
		`atomicdetonators` int(8) NOT NULL,
		`corbomitedevices` int(8) NOT NULL,
		`subspaceetherprobes` int(8) NOT NULL,
		`transporterrange` int(8) NOT NULL,
		`offensiveodds` varchar(8) NOT NULL,
		`defensiveodds` varchar(8) NOT NULL,
		`scannerdensity` int(1) NOT NULL,
		`scannerholo` int(1) NOT NULL,
		`transwarpdrive` int(1) NOT NULL,
		`fusiondrive` int(1) NOT NULL,
		`planetscanner` int(1) NOT NULL,
		`interdictorgenerator` int(1) NOT NULL,
		`usedasescapepod` int(1) NOT NULL,
		`carriesescapepod` int(1) NOT NULL,
		`escapepodclass` int(8) NOT NULL,
		`canlandonplanet` int(1) NOT NULL,
		`defensiveguardianbonus` int(1) NOT NULL,
		`requirefedcommission` int(1) NOT NULL,
		`requiredxp` int(8) NOT NULL,
		`requirecorporatestatus` int(1) NOT NULL,
		`requireceostatus` int(1) NOT NULL,
		`costofholdspace` varchar(8) NOT NULL,
		`costofdrive` varchar(8) NOT NULL,
		`costofcomputersystem` varchar(8) NOT NULL,
		`costofshipshull` varchar(8) NOT NULL
	)"""
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `shipclass` ADD PRIMARY KEY (`shcid`);"
	db.query(connection, query)

	connection = db.stdb()
	query = "ALTER TABLE `shipclass` MODIFY `shcid` int(128) NOT NULL AUTO_INCREMENT;"
	db.query(connection, query)

	# Insert ships
	'''
	Escape Pod
	Class F Shuttle
	Cargo Ship
	Daedelus
	Saladin
	Reliant
	Constitution
	Federation
	'''
	query = "INSERT INTO `shipclass` (`shipclassname`, `fgcolour`, `bgcolour`, `alignment`, `manufacturer`, `cargoholdsstart`, `cargoholdsmax`, `fightersstart`, `fightersmax`, `fighterattackforce`, `photontorpedoesstart`, `photontorpedoesmax`,  `shieldsstart`, `shieldsmax`, `minesstart`, `minesmax`, `minedisruptorsstart`, `minedisruptorsmax`, `markerbeaconsstart`, `markerbeaconsmax`, `genesistorpedoes`, `cloakingdevices`, `atomicdetonators`, `corbomitedevices`,`subspaceetherprobes`, `transporterrange`, `offensiveodds`, `defensiveodds`, `scannerdensity`, `scannerholo`, `transwarpdrive`, `fusiondrive`, `planetscanner`, `interdictorgenerator`, `usedasescapepod`, `carriesescapepod`, `escapepodclass`, `canlandonplanet`, `defensiveguardianbonus`, `requirefedcommission`, `requiredxp`, `requirecorporatestatus`, `requireceostatus`, `costofholdspace`, `costofdrive`, `costofcomputersystem`, `costofshipshull`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	func.moduleload('shipclass', query)