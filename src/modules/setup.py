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
    query = "CREATE TABLE `players` (`pid` int(24) NOT NULL, `callsign` varchar(128) NOT NULL, `fname` varchar(128) NOT NULL, `mname` varchar(128) NOT NULL, `lname` varchar(128) NOT NULL, `alignement` varchar(128) NOT NULL,`rank` int(4) NOT NULL, `branch` int(3) NOT NULL, `xp` int(128) NOT NULL, `kills` int(128) NOT NULL, `deaths` int(128) NOT NULL,`locationx` int(24) NOT NULL,`locationy` int(24) NOT NULL, `whereami` int(24) NOT NULL, `health` int(24) NOT NULL, `species` int(24) NOT NULL, `age` int(24) NOT NULL, `birthday` int(24) NOT NULL, `homeplanet` int(24) NOT NULL, `languages` int(24) NOT NULL, `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, `lastlogin` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
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

    # Create the Civilizations table table
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
