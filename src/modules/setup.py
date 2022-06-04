# Import the required modules.
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art

# First time setup


def setup():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
            # database='startrek'
        )
        # print("Connection to MySQL DB successful")
    except Error as e:
        # print(f"The error '{e}' occurred")
        connection = "FALSE"

    query = "CREATE DATABASE IF NOT EXISTS `startrek`"
    db.query(connection, query)
    art.cd(23, '', "Game database created.", "reset", True)

    # Create User Table
    connection = db.stdb()
    query = "CREATE TABLE `players` (`pid` int(24) NOT NULL, `callsign` varchar(128) NOT NULL, `fname` varchar(128) NOT NULL, `mname` varchar(128) NOT NULL, `lname` varchar(128) NOT NULL, `alignment` varchar(128) NOT NULL,`rank` int(4) NOT NULL, `branch` varchar(16) NOT NULL, `xp` int(128) NOT NULL, `kills` int(128) NOT NULL, `deaths` int(128) NOT NULL,`locationx` int(24) NOT NULL,`locationy` int(24) NOT NULL, `whereami` varchar(24) NOT NULL, `health` int(24) NOT NULL, `species` varchar(24) NOT NULL, `age` int(24) NOT NULL, `birthday` varchar(24) NOT NULL, `homeplanet` varchar(24) NOT NULL, `languages` varchar(24) NOT NULL, `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, `lastlogin` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `players` ADD PRIMARY KEY (`pid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `players` MODIFY `pid` int(24) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(24, '', "User Directory generated.", "reset", True)

    # Create High Scores Table
    connection = db.stdb()
    query = "CREATE TABLE `highscores` (`hsid` int(2) NOT NULL, `pid` int(9) NOT NULL, `score` int(64) NOT NULL, `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `highscores` ADD PRIMARY KEY (`hsid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `highscores` MODIFY `hsid` int(2) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(25, '', "High Scores Board built.", "reset", True)

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

    art.cd(25, '', "Galactic Fabric woven.", "reset", True)

    # Create Star Types Table
    connection = db.stdb()
    query = "CREATE TABLE `starclass` (`scid` int(2) NOT NULL, `starclass` varchar(1) NOT NULL, `colour` varchar(7) NOT NULL)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `starclass` ADD PRIMARY KEY (`scid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `starclass` MODIFY `scid` int(2) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    connection = db.stdb()
    starclasses = [('1', 'O', '#9bb0ff'), ('2', 'B', '#aabfff'), ('3', 'A', '#cad7ff'),
                   ('4', 'F', '#f8f7ff'), ('5', 'G', '#fff4ea'), ('6', 'K', '#ffd2a1'), ('7', 'M', '#ffcc6f')]

    query = "INSERT INTO `starclass` (`scid`, `starclass`, `colour`) VALUES (%s, %s, %s)"
    db.querymany(connection, query, starclasses)

    # Create the Stars table
    #! Not sure if we need secid. See the 'Galaxy' table above.
    connection = db.stdb()
    query = "CREATE TABLE `stars` (`sid` int(128) NOT NULL, `secid` int(128), `x` int(128) NOT NULL, `y` int(128) NOT NULL, `starname` varchar(128), `scid` varchar(1) NOT NULL)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `stars` ADD PRIMARY KEY (`sid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `stars` MODIFY `sid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(26, '', "Stellar matter formed.", "reset", True)

    # Create Planet Types Table
    connection = db.stdb()
    query = "CREATE TABLE `planetclass` (`pcid` int(2) NOT NULL, `planetclass` varchar(1) NOT NULL, `Description` varchar(512) NOT NULL, `colour` varchar(7) NOT NULL)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `planetclass` ADD PRIMARY KEY (`pcid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `planetclass` MODIFY `pcid` int(2) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    connection = db.stdb()
    planetclasses = [("1", "D", "An uninhabitable planetoid, moon, or small planet with little to no atmosphere. Some were viable candidates for terraforming.", "249"), ("2", "H", "Generally uninhabitable for Humans, though viable for Sheliak.", "172"), ("3", "J", "A type of gas giant.", "226"), ("4", "K", "	Adaptable for Humans by use of artificial biospheres.", "19"), ("5", "L", "Marginally habitable, with vegetation but usually no animal life.", "22"), (
        "6", "M", "Earth-like, with atmospheres containing oxygen and, typically, nucleogenic particles. Largely habitable for humanoid life forms.", "46"), ("7", "N", "A sulfuric planet.", "100"), ("8", "R", "A rogue planet, not as habitable as a terrestrial planet.", "237"), ("9", "T", "A type of gas giant.", "179"), ("10", "Y", "A world with a toxic atmosphere and surface temperatures exceeding 500 Kelvin. Prone to thermionic radiation discharges.", "196")]
    query = "INSERT INTO `planetclass` (`pcid`, `planetclass`, `description`, `colour`) VALUES (%s, %s, %s, %s)"
    db.querymany(connection, query, planetclasses)

    # Create the Planets table
    #! Not sure if we need secid. See the 'Galaxy' table above.
    connection = db.stdb()
    query = "CREATE TABLE `planets` (`pid` int(128) NOT NULL, `secid` int(128), `x` int(128) NOT NULL, `y` int(128) NOT NULL, `sid` int(128), `planetname` varchar(128), `pcid` varchar(2) NOT NULL, `cid` varchar(128) NOT NULL DEFAULT '0')"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `planets` ADD PRIMARY KEY (`pid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `planets` MODIFY `pid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(27, '', "Aligning planet orbits.", "reset", True)

    # Create the Civilizations table
    connection = db.stdb()
    query = "CREATE TABLE `civilizations` (`cid` int(128) NOT NULL, `secid` int(128), `x` int(128) NOT NULL, `y` int(128) NOT NULL, `civname` varchar(128))"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `civilizations` ADD PRIMARY KEY (`cid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `civilizations` MODIFY `cid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(28, '', "Creating the conditions for life.", "reset", True)

    # Create the Logs table
    connection = db.stdb()
    query = "CREATE TABLE `logs` (`lid` int(128) NOT NULL, `logtype` varchar(24), `log` varchar(128) NOT NULL, `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `logs` ADD PRIMARY KEY (`lid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `logs` MODIFY `lid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(29, '', "Starting the historic record.", "reset", True)

    # Create Port Classes Table
    '''
    Port classes are a function of size, not what they trade in.
    The first 3 classes (0,1,2) will offer shipyard services, the number of services reducing the lower the class goes.

    '''
    connection = db.stdb()
    query = "CREATE TABLE `portclass` (`pcid` int(8) NOT NULL, `portclass` varchar(8) NOT NULL, `orecap` varchar(7) NOT NULL, `organicscap` varchar(7) NOT NULL, `equipmentcap` varchar(7) NOT NULL, `theater` int(1) NOT NULL, `bank` int(1) NOT NULL, `techdealer` int(1) NOT NULL, `police` int(1) NOT NULL, `shipyards` int(1) NOT NULL, `tavern` int(1) NOT NULL, `library` int(1) NOT NULL, `blackmarket` int(1) NOT NULL, `bar` int(1) NOT NULL, `description` varchar(1024) NOT NULL)"
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
    connection = db.stdb()
    portclasses = [('0', '10000', '10000', '10000', '1', '1', '1', '1', '1', '0', '1', '0', '0', "What never ceases to amaze you is the massive scale of the Class 0 port. There is enough space to house over 15,000 officers and up to 35,000 visitors at any given time. Nearly any service you can think of exists on a Class 0 port. You return your focus to docking your ship, as you don't want to be known as the person who scratched their paint on the station."), ('1', '8500', '8500', '8500', '0', '1', '1', '1', '0', '0', '0', '0', '0', "Class 1 ports serve as major regional hubs in deep space. With large cargo space, they are excellent trade centers for traders looking to make a profit. Most services you can require are found on a Class 1 port."), ('2', '7500', '7500', '7500', '0', '1', '1', '1', '0', '0', '0', '0', '0', "Class 2"),
                   ('3', '7000', '7000', '7000', '0', '0', '0', '0', '0', '0', '0', '0', '0', "Class 3"), ('4', '6000', '6000', '6000', '0', '0', '0', '0', '0', '0', '0', '0', '0', "Class 4"), ('5', '5000', '5000', '5000', '0', '0', '0', '0', '0', '0', '0', '0', '0', "Class 5"), ('6', '4000', '4000', '4000', '0', '0', '0', '0', '0', '0', '0', '0', '0', "Class 6"), ('7', '3000', '3000', '3000', '0', '0', '0', '0', '0', '0', '0', '0', '1', "Class 7"), ('8', '2000', '2000', '2000', '0', '0', '0', '0', '0', '0', '0', '0', '1', "Class 8"), ('9', '1000', '1000', '1000', '0', '0', '1', '0', '0', '1', '0', '1', '1', "The smallest station type in the galaxy is the Class 9, which can often be found in frontier space or near underdeveloped planets. The distance of these ports from well-regulated space makes them a haven for the...more shadowy citizens of the galaxy.")]

    query = "INSERT INTO `portclass` (`portclass`, `orecap`, `organicscap`, `equipmentcap`, `theater`, `bank`, `techdealer`, `police`, `shipyards`, `tavern`, `library`, `blackmarket`, `bar`, `description`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    db.querymany(connection, query, portclasses)

    # Create the Ports table
    connection = db.stdb()
    query = "CREATE TABLE `ports` (`portid` int(128) NOT NULL, `portclass` int(8) NOT NULL, `portname` varchar(128) NOT NULL, `locationx` int(16) NOT NULL, `locationy` int(16) NOT NULL, `orecount` INT(5) NOT NULL, `organicscount` INT(5) NOT NULL, `equipmentcount` INT(5) NOT NULL, `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `ports` ADD PRIMARY KEY (`portid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `ports` MODIFY `portid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    # Last Time Docked
    connection = db.stdb()
    query = "CREATE TABLE `portlastdocked` (`ldapid` int(128) NOT NULL, `portid` int(8), `pid` int(8) NOT NULL, `lastdockeddate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `portlastdocked` ADD PRIMARY KEY (`ldapid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `portlastdocked` MODIFY `ldapid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(30, '', "Placing safe harbours throughout the galaxy.", "reset", True)

    # Ship Class table
    connection = db.stdb()
    query = "CREATE TABLE `shipclass` (`shcid` int(128) NOT NULL, `shipclassname` varchar(32) NOT NULL, `fgcolour` int(7) NOT NULL, `bgcolour` int(7) NOT NULL, `alignment` varchar(24), `manufacturer` varchar(48), `cargoholdsstart` int(8) NOT NULL, `cargoholdsmax` int(8) NOT NULL, `fightersstart` int(8) NOT NULL, `fightersmax` int(8) NOT NULL, `fighterattackforce` int(8) NOT NULL, `photontorpedoesstart` int(8) NOT NULL, `photontorpedoesmax` int(8) NOT NULL, `shieldsstart` int(8) NOT NULL, `shieldsmax` int(8) NOT NULL, `minesstart` int(8) NOT NULL, `minesmax` int(8) NOT NULL, `minedisruptorsstart` int(8) NOT NULL, `minedisruptorsmax` int(8) NOT NULL, `markerbeaconsstart` int(8) NOT NULL, `markerbeaconsmax` int(8) NOT NULL, `genesistorpedoes` int(8) NOT NULL, `cloakingdevices` int(8) NOT NULL, `atomicdetonators` int(8) NOT NULL, `corbomitedevices` int(8) NOT NULL, `subspaceetherprobes` int(8) NOT NULL, `transporterrange` int(8) NOT NULL, `offensiveodds` varchar(8) NOT NULL, `defensiveodds` varchar(8) NOT NULL, `scannerdensity` int(1) NOT NULL, `scannerholo` int(1) NOT NULL, `transwarpdrive` int(1) NOT NULL, `fusiondrive` int(1) NOT NULL, `planetscanner` int(1) NOT NULL, `interdictorgenerator` int(1) NOT NULL, `usedasescapepod` int(1) NOT NULL, `carriesescapepod` int(1) NOT NULL, `escapepodclass` int(8) NOT NULL, `canlandonplanet` int(1) NOT NULL, `defensiveguardianbonus` int(1) NOT NULL, `requirefedcommission` int(1) NOT NULL, `requiredxp` int(8) NOT NULL, `requirecorporatestatus` int(1) NOT NULL, `requireceostatus` int(1) NOT NULL, `costofholdspace` varchar(8) NOT NULL, `costofdrive` varchar(8) NOT NULL, `costofcomputersystem` varchar(8) NOT NULL, `costofshipshull` varchar(8) NOT NULL)"
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
    connection = db.stdb()
    shipclasses = [('*** Escape Pod ***', '27', '999', '2', 'Federation Shipyards', '1', '5', '1', '50', '25', '0', '0', '15', '50', '0', '0', '50', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0.5', '0.5', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '500', '4246', '4700', '5000'), ('Saladin',
                                                                                                                                                                                                                                                                                                                            '2', '999', '2', 'Federation Shipyards', '20', '75', '30', '2500', '750', '5', '25', '100', '400', '0', '50', '0', '10', '10', '50', '5', '0', '5', '1500', '25', '5', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '10000', '1000', '20300', '10000'), ('Constitution',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             '255', '27', '2', 'Federation Shipyards', '40', '150', '10000', '50000', '10000', '5', '50', '2000', '10000', '0', '125', '10', '10', '150', '150', '10', '0', '0', '1500', '5', '15', '1.5', '1.5', '1', '1', '1', '0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '23000', '10000', '231000', '65000')]

    query = "INSERT INTO `shipclass` (`shipclassname`, `fgcolour`, `bgcolour`, `alignment`, `manufacturer`, `cargoholdsstart`, `cargoholdsmax`, `fightersstart`, `fightersmax`, `fighterattackforce`, `photontorpedoesstart`, `photontorpedoesmax`,  `shieldsstart`, `shieldsmax`, `minesstart`, `minesmax`, `minedisruptorsstart`, `minedisruptorsmax`, `markerbeaconsstart`, `markerbeaconsmax`, `genesistorpedoes`, `cloakingdevices`, `atomicdetonators`, `corbomitedevices`,`subspaceetherprobes`, `transporterrange`, `offensiveodds`, `defensiveodds`, `scannerdensity`, `scannerholo`, `transwarpdrive`, `fusiondrive`, `planetscanner`, `interdictorgenerator`, `usedasescapepod`, `carriesescapepod`, `escapepodclass`, `canlandonplanet`, `defensiveguardianbonus`, `requirefedcommission`, `requiredxp`, `requirecorporatestatus`, `requireceostatus`, `costofholdspace`, `costofdrive`, `costofcomputersystem`, `costofshipshull`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    db.querymany(connection, query, shipclasses)

    # Ships table
    connection = db.stdb()
    query = "CREATE TABLE `ships` (`shid` int(128) NOT NULL, `shipname` varchar(32) NOT NULL, `ownedby` int(16) NOT NULL, `active` int(16) NOT NULL, `ports` int(16) NOT NULL, `kills` int(16), `shipclass` int(128), `cloaked` int(1) NOT NULL, `locationx` int(128) NOT NULL, `locationy` int(128) NOT NULL, `fighters` int(16) NOT NULL, `shields` int(8) NOT NULL, `holds` int(8) NOT NULL, `invfuelore` int(8) NOT NULL, `invorganics` int(8) NOT NULL, `invequipment` int(8) NOT NULL, `invcolonists` int(8) NOT NULL, `genesistorpedoes` int(8) NOT NULL, `mines` int(8) NOT NULL, `markerbeacons` int(8) NOT NULL, `holoscanner` int(1) NOT NULL, `transwarpdrive` int(1) NOT NULL, `onplanetnum` int(16) NOT NULL, `cloakingdevices` int(8) NOT NULL, `interdicting` int(1) NOT NULL, `atomicdetonators` int(8) NOT NULL, `corbomitedevices` int(8) NOT NULL, `subspaceetherprobes` int(8) NOT NULL, `minedisruptors` int(8) NOT NULL, `photontorpedoes` int(8) NOT NULL, `psychicprobe` int(1) NOT NULL, `planetscanner` int(1) NOT NULL)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `ships` ADD PRIMARY KEY (`shid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `ships` MODIFY `shid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(31, '', "Finalizing ship blueprints.", "reset", True)
