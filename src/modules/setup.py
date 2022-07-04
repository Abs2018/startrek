# Import the required modules.
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
import os
import platform
from csv import reader

# This module will read the CSV files in the data directory and import the values in them to their respective tables.


def moduleload(folder, query):
    # Get the path for the system
    opsys = (platform.system())
    modpath = str(os.getcwd())
    if opsys == "Windows":  # I believe Windows is the only OS that uses \
        slash = "\\"
    else:  # All other OS's use /.
        slash = "/"
    modpath = modpath+slash+'data'+slash+folder+slash
    # print(modpath)
    # Define the list to be saved
    folderclass = []
    # Get the file listing in the folder variable and put it in a list
    for mod in os.listdir(modpath):
        sample = modpath + '_Sample.txt'
        # Check if current mod is a file
        if os.path.isfile(os.path.join(modpath, mod)):
            # Avoid the sample file
            if os.path.join(modpath, mod) != sample:
                # Open each file and save its contents in a dictionary
                f = open(os.path.join(modpath, mod), "r", encoding="utf8")
                csv_reader = reader(f)
                for row in csv_reader:
                    folderclass.append(row)
                f.close()
    # print(folderclass)
    # Insert into database
    connection = db.stdb()
    db.querymany(connection, query, folderclass)


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

    colour = 23

    query = "CREATE DATABASE IF NOT EXISTS `startrek`"
    db.query(connection, query)
    art.cd(colour, '', "Game database created.", "reset", True)
    colour = colour + 1

    # Create User Table
    connection = db.stdb()
    query = "CREATE TABLE `players` (`pid` int(24) NOT NULL, `callsign` varchar(128) NOT NULL, `fname` varchar(128) NOT NULL, `mname` varchar(128) NOT NULL, `lname` varchar(128) NOT NULL, `alignment` varchar(128) NOT NULL, `morality` varchar(16) NOT NULL,`rank` int(4) NOT NULL, `branch` varchar(16) NOT NULL, `xp` int(128) NOT NULL, `kills` int(128) NOT NULL, `deaths` int(128) NOT NULL,`locationx` int(24) NOT NULL,`locationy` int(24) NOT NULL, `whereami` varchar(24) NOT NULL, `health` int(24) NOT NULL, `species` varchar(24) NOT NULL, `age` int(24) NOT NULL, `birthday` varchar(24) NOT NULL, `homeplanet` varchar(24) NOT NULL, `languages` varchar(24) NOT NULL, `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, `lastlogin` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `players` ADD PRIMARY KEY (`pid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `players` MODIFY `pid` int(24) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(colour, '', "User Directory generated.", "reset", True)
    colour = colour + 1

    # Create Settings Table
    connection = db.stdb()
    query = "CREATE TABLE `settings` (`sid` int(24) NOT NULL, `settingname` varchar(128) NOT NULL, `settingvalue` varchar(128) NOT NULL, `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `settings` ADD PRIMARY KEY (`sid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `settings` MODIFY `sid` int(24) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(colour, '', "Game Settings prepared.", "reset", True)
    colour = colour + 1

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

    art.cd(colour, '', "High Scores Board built.", "reset", True)
    colour = colour + 1

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
    colour = colour + 1

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
    query = "INSERT INTO `starclass` (`starclass`, `colour`) VALUES (%s, %s)"
    moduleload('starclass', query)

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

    art.cd(colour, '', "Stellar matter formed.", "reset", True)
    colour = colour + 1

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

    query = "INSERT INTO `planetclass` (`planetclass`, `description`, `colour`) VALUES (%s, %s, %s)"
    moduleload('planetclass', query)

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

    art.cd(colour, '', "Aligning planet orbits.", "reset", True)
    colour = colour + 1

    # Create the Empires table
    connection = db.stdb()
    query = "CREATE TABLE `empires` (`eid` int(128) NOT NULL, `secid` int(128), `x` int(128) NOT NULL, `y` int(128) NOT NULL, `empname` varchar(128))"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `empires` ADD PRIMARY KEY (`eid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `empires` MODIFY `eid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    art.cd(colour, '', "Creating the conditions for life.", "reset", True)
    colour = colour + 1

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

    art.cd(colour, '', "Starting the historic record.", "reset", True)
    colour = colour + 1

    # Create the Race table
    connection = db.stdb()
    query = "CREATE TABLE `raceclass` (`rid` int(128) NOT NULL, `raceclass` varchar(128) NOT NULL, `description` varchar(4096), `strength` int(3) NOT NULL, `endurance` int(3) NOT NULL, `intellect` varchar(3) NOT NULL, `dexterity` varchar(3) NOT NULL, `charisma` varchar(3) NOT NULL, `luck` varchar(3) NOT NULL, `psionic` varchar(3) NOT NULL, `homeworld` varchar(128) NOT NULL, `empire` varchar(128) NOT NULL)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `raceclass` ADD PRIMARY KEY (`rid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `raceclass` MODIFY `rid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    query = "INSERT INTO `raceclass` (`raceclass`, `description`, `strength`, `endurance`, `intellect`, `dexterity`, `charisma`, `luck`, `psionic`, `homeworld`, `empire`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    moduleload('raceclass', query)

    art.cd(colour, '', "Evolving species.", "reset", True)
    colour = colour + 1

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
    query = "INSERT INTO `portclass` (`portclass`, `orecap`, `organicscap`, `equipmentcap`, `theater`, `bank`, `techdealer`, `police`, `shipyards`, `tavern`, `library`, `blackmarket`, `bar`, `description`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    moduleload('portclass', query)

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

    art.cd(colour, '', "Placing safe harbours throughout the galaxy.", "reset", True)
    colour = colour + 1

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
    query = "INSERT INTO `shipclass` (`shipclassname`, `fgcolour`, `bgcolour`, `alignment`, `manufacturer`, `cargoholdsstart`, `cargoholdsmax`, `fightersstart`, `fightersmax`, `fighterattackforce`, `photontorpedoesstart`, `photontorpedoesmax`,  `shieldsstart`, `shieldsmax`, `minesstart`, `minesmax`, `minedisruptorsstart`, `minedisruptorsmax`, `markerbeaconsstart`, `markerbeaconsmax`, `genesistorpedoes`, `cloakingdevices`, `atomicdetonators`, `corbomitedevices`,`subspaceetherprobes`, `transporterrange`, `offensiveodds`, `defensiveodds`, `scannerdensity`, `scannerholo`, `transwarpdrive`, `fusiondrive`, `planetscanner`, `interdictorgenerator`, `usedasescapepod`, `carriesescapepod`, `escapepodclass`, `canlandonplanet`, `defensiveguardianbonus`, `requirefedcommission`, `requiredxp`, `requirecorporatestatus`, `requireceostatus`, `costofholdspace`, `costofdrive`, `costofcomputersystem`, `costofshipshull`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    moduleload('shipclass', query)

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

    art.cd(colour, '', "Finalizing ship blueprints.", "reset", True)
    colour = colour + 1

    # Ranks table
    connection = db.stdb()
    query = "CREATE TABLE `ranks` (`rid` int(128) NOT NULL, `rankname` varchar(32) NOT NULL, `rankxp` int(16) NOT NULL, `empire` int(16) NOT NULL)"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `ranks` ADD PRIMARY KEY (`rid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `ranks` MODIFY `rid` int(128) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)

    rankclasses = [('Private', '2', '1'), ('Private 1st Class', '4', '1'), ('Lance Corporal', '6', '1'), ('Corporal', '16', '1'), ('Sargeant', '32', '1'), ('Staff Sargeant', '64', '1'), ('Gunnery Sargeant', '128', '1'), ('1st Sargeant', '256', '1'), ('Sargeant Major', '512', '1'), ('Warrant Officer', '1024', '1'), ('Chief Warrant Officer', '2048', '1'), ('Ensign', '4096', '1'), ('Lieutenant J.G.', '8192', '1'), ('Lieutenant', '16384', '1'), ('Lieutenant Commander', '32768', '1'), ('Commander', '65536', '1'), ('Captain', '131072', '1'), ('Commodore', '262144', '1'), ('Rear Admiral', '524288', '1'), ('Vice Admiral', '1048576', '1'), ('Admiral', '2097152', '1'), ('Fleet Admiral', '4194304', '1'), ('Nuisance 3rd Class', '2', '2'),
                   ('Nuisance 2nd Class', '4', '2'), ('Nuisance 1st Class', '6', '2'), ('Menace 3rd Class', '16', '2'), ('Menace 2nd Class', '32', '2'), ('Menace 1st Class', '64', '2'), ('Smuggler 3rd Class', '128', '2'), ('Smuggler 2nd Class', '256', '2'), ('Smuggler 1st Class', '512', '2'), ('Smuggler Savant', '1024', '2'), ('Robber', '2048', '2'), ('Terrorist', '4096', '2'), ('Pirate', '8192', '2'), ('Infamous Pirate', '16384', '2'), ('Notorious Pirate', '32768', '2'), ('Dread Pirate', '65536', '2'), ('Galactic Scourge', '131072', '2'), ('Enemy of the State', '262144', '2'), ('Enemy of the People', '524288', '2'), ('Enemy of Humankind', '1048576', '2'), ('Heinous Overlord', '2097152', '2'), ('Prime Evil', '4194304', '2')]
    connection = db.stdb()
    query = "INSERT INTO `ranks` (`rankname`, `rankxp`, `empire`) VALUES (%s, %s, %s)"
    db.querymany(connection, query, rankclasses)

    art.cd(colour, '', "Organizing the rank and file.", "reset", True)
    colour = colour + 1
