# setup.py will create the database, tables, and import the mods into the game.
# We have broken up the tables into separate scripts because it is easier
# to keep the script cleaner, and swap out tables if necessary while developing.

# Import the required modules.
from modules.tables import database
from modules.tables import userAttributesAndSkillsTable
from modules.tables import userTable
from modules.tables import settingsTable
from modules.tables import highScoresTable
from modules.tables import galaxyTable
from modules.tables import starClassTable
from modules.tables import starsTable
from modules.tables import planetClassTable
from modules.tables import planetsTable
from modules.tables import empiresTable
from modules.tables import logsTable
from modules.tables import raceClassTable
from modules.tables import portClassTable
from modules.tables import portsTable
from modules.tables import lastDockedTable
from modules.tables import shipClassTable
from modules.tables import shipsTable
from modules.tables import ranksTable

# First time setup


def setup():
    # The colours are added to make the text look interesting.
    # You can get rid of the += if you want a single colour.
    colour = 23
    # Create the database.
    database.createDatabase(colour)
    colour = colour + 1
    # Create the players attributes and skills table
    userAttributesAndSkillsTable.createUserAttributesAndSkillsTable()
    # Create the players table
    userTable.createUserTable(colour)
    colour = colour + 1
    # Create the table that holds the Settings key => value pairs.
    settingsTable.createSettingsTable(colour)
    colour = colour + 1
    # Create table that stores the high scores
    highScoresTable.createHighScoresTable(colour)
    colour = colour + 1
    # Create the Galaxy Table
    galaxyTable.createGalaxyTable(colour)
    colour = colour + 1
    # Create the Star Classes
    starClassTable.createStarClassTable()
    # Create the Stars Table
    starsTable.createStarsTable(colour)
    colour = colour + 1
    # Create the Planet Classes
    planetClassTable.createPlanetClass()
    # Create the Planets table
    planetsTable.createPlanetsTable(colour)
    colour = colour + 1
    # Create the Empires table
    empiresTable.createEmpiresTable(colour)
    colour = colour + 1
    # Create the Logs table
    logsTable.createLogsTable(colour)
    colour = colour + 1
    # Create the Race Class Table
    raceClassTable.createRaceClassTable(colour)
    colour = colour + 1
    # Create the Ports Classes
    portClassTable.createPortClass()
    # Create the Ports table
    portsTable.createPortsTable()
    # Create the Last Docked Table
    lastDockedTable.createLastDockedTable(colour)
    colour = colour + 1
    # Create the Ship Class Table
    shipClassTable.createShipClassTable()
    shipsTable.createShipsTable(colour)
    colour = colour + 1
    # Create the Ranks Table
    ranksTable.createRanksTable(colour)
    colour = colour + 1
