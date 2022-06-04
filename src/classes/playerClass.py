from classes import shipClass
from dataclasses import dataclass
from os import getpid
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
from classes import log
log = log.log()
shipClass = shipClass.shipClass()

# TODO:
# * Check to make sure that the user's first name is not 'q'


@dataclass
class player():
    def __init__(self):
        pass

    def check(self):
        # Get the player name.
        art.cd(13, '', "", '', False)
        callsign = ''
        while True:
            print("")
            callsign = input("What is your callsign? ")
            if callsign:
                break
        art.cd(4, '', "", 0, False)
        # Check the DB for player.
        connection = db.stdb()
        query = "select * from `players` where `callsign` = '"+callsign+"'"
        results = db.rowcount(connection, query)
        if results == 0:
            # Register player
            print("")
            art.cd(2, '', "You were not found in the player database.", '', True)
            print("")
            art.cd(
                255, 4, "Would you like to start a new character in this game? (Type ", '', False)
            art.cd(3, '', "Y", '', False)
            art.cd(255, 4, " or ", '', False)
            art.cd(3, '', "N", '', False)
            art.cd(255, 4, ")", 0, False)
            art.cd('cyan', '', '', '', True)
            command = input("")
            if command == "y" or command == "Y" or command == "":
                player.create(callsign)
                # Get the PID
                connection = db.stdb()
                query = "select * from `players` where `callsign` = '"+callsign+"'"
                results = db.query(connection, query)
                for row in results:
                    pid = row['pid']
            elif command == "N" or command == "n":
                print("")
                art.cd(2, '', "Maybe next time...", 0, True)
                print("")
                quit()
        else:
            # Get the PID
            connection = db.stdb()
            query = "select * from `players` where `callsign` = '"+callsign+"'"
            results = db.query(connection, query)
            for row in results:
                pid = row['pid']
        return pid

    def create(callsign):
        # Create the player.
        print("")
        art.cd(3, '', "Great! ", '', False)
        art.cd(
            'cyan', '', "Let's get some paperwork out of the way.", '', True)
        print("")
        art.cd('cyan', '', "What is your first name? ", 0, True)
        fname = input("")
        art.cd(
            'cyan', '', "If you have a middle name, let me know. Press 'Enter' to skip. ", 0, True)
        mname = input("")
        art.cd(
            'cyan', '', "Last, but not least, what is your last name? ", 0, True)
        lname = input("")
        branch = ""
        while branch == "":
            art.cd(
                'cyan', '', "Which branch of service are you most interested in? (", '', False)
            art.cd(3, '', "Command", '', False)
            art.cd('cyan', '', ", ", '', False)
            art.cd(4, '', "Sciences", '', False)
            art.cd('cyan', '', ", or ", '', False)
            art.cd(1, '', "Operations", '', False)
            art.cd('cyan', '', ") ", 0, True)
            branch = input("")
            match branch:
                case "Command":
                    branch = "Command"
                case "command":
                    branch = "Command"
                case "Sciences":
                    branch = "Sciences"
                case "sciences":
                    branch = "Sciences"
                case "Operations":
                    branch = "Operations"
                case "operations":
                    branch = "Operations"
                case _:
                    branch = ""
        # Save the player name.
        alignment = "Federation"
        rank = 1
        xp = 0
        kills = 0
        deaths = 0
        locationx = 0
        locationy = 0
        whereami = "station"
        health = 100
        species = "Human"
        age = 22
        birthday = "24/04"
        homeplanet = "Earth"
        languages = "English"
        # Create the player
        connection = db.stdb()
        query = "INSERT INTO `players` (`callsign`, `fname`, `mname`, `lname`, `alignment`, `rank`, `branch`, `xp`, `kills`, `deaths`, `locationx`, `locationy`, `whereami`, `health`, `species`, `age`, `birthday`, `homeplanet`, `languages`) VALUES ('"+str(callsign)+"', '"+str(fname)+"', '"+str(mname)+"', '"+str(
            lname)+"', '"+str(alignment)+"', '"+str(rank)+"', '"+str(branch)+"', '"+str(xp)+"', '"+str(kills)+"', '"+str(deaths)+"', '"+str(locationx)+"', '"+str(locationy)+"', '"+str(whereami)+"', '"+str(health)+"', '"+str(species)+"', '"+str(age)+"', '"+str(birthday)+"', '"+str(homeplanet)+"', '"+str(languages)+"')"
        # print(query)
        db.query(connection, query)

        # Get the player's PID
        pid = getpid(callsign)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Get the ship class number for the Saladin

        # Ask for the ship name

        # Launch the shipCreate(pid, shipname, shipclass) function to assign the player to a ship.

        print("")
        art.cd(
            'cyan', '', "Give me a moment to sign you in...Okay, you're all set!", '', True)

        # Log the event
        connection = db.stdb()
        logtype = "NEWPLAYER"
        logevent = fname + " " + lname + " joined the " + alignment + "!"
        log.logAdd(logtype, logevent)

    def getpid(self, callsign):
        connection = db.stdb()
        query = "SELECT `pid` FROM `players` WHERE `callsign` = '" + \
            str(callsign)+"'"
        db.query(connection, query)

    def changecallsign(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Callsign:", 0, False)
            callsign = input(" ")
            if callsign:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `callsign`='" + \
            callsign+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return callsign

    def changefname(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New First Name:", 0, False)
            fname = input(" ")
            if fname:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `fname`='" + \
            fname+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return fname

    def changemname(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Middle Name:", 0, False)
            mname = input(" ")
            if mname:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `mname`='" + \
            mname+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return mname

    def changelname(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Last Name:", 0, False)
            lname = input(" ")
            if lname:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `lname`='" + \
            lname+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return lname

    def changealignment(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Alignment:", 0, False)
            alignment = input(" ")
            if alignment:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `alignment`='" + \
            alignment+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return alignment

    def changerank(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Rank:", 0, False)
            rank = input(" ")
            if rank:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `rank`='" + \
            rank+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return rank

    def changebranch(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Branch:", 0, False)
            branch = input(" ")
            if branch:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `branch`='" + \
            branch+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return branch

    # Changes the total XP
    def changexp(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Experience Amount:", 0, False)
            xp = input(" ")
            if xp:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `xp`='" + \
            xp+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return xp

    def changekills(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Kill Count:", 0, False)
            kills = input(" ")
            if kills:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `kills`='" + \
            kills+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return kills

    def changedeaths(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "New Death Count:", 0, False)
            deaths = input(" ")
            if deaths:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `deaths`='" + \
            deaths+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return deaths

    # This changes the X coordinate from the user editor.
    def changelocationx(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Update X Coordinate:", 0, False)
            locationx = input(" ")
            if locationx:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `locationx`='" + \
            locationx+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return locationx

    # This changes the y coordinate from the user editor.
    def changelocationy(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Update Y Coordinate:", 0, False)
            locationy = input(" ")
            if locationy:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `locationy`='" + \
            locationy+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return locationy

    def changewhereami(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Update Where I Am:", 0, False)
            whereami = input(" ")
            if whereami:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `whereami`='" + \
            whereami+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return whereami

    def changehealth(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Update Health:", 0, False)
            health = input(" ")
            if health:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `health`='" + \
            health+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return health

    def changespecies(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Change Species:", 0, False)
            species = input(" ")
            if species:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `species`='" + \
            species+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return species

    def changeage(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Change Age:", 0, False)
            age = input(" ")
            if age:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `age`='" + \
            age+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return age

    def changebirthday(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Change Birthday:", 0, False)
            birthday = input(" ")
            if birthday:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `birthday`='" + \
            birthday+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return birthday

    def changehomeplanet(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Change Home Planet:", 0, False)
            homeplanet = input(" ")
            if homeplanet:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `homeplanet`='" + \
            homeplanet+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return homeplanet

    def changelanguage(self, pid):
        while True:
            print("")
            art.cd('light_cyan', '', "Change Language:", 0, False)
            languages = input(" ")
            if languages:
                break
        connection = db.stdb()
        query = "UPDATE `players` SET `languages`='" + \
            languages+"' WHERE `pid`='"+str(pid)+"'"
        # print(query)
        db.query(connection, query)
        return languages

    # This changes the coordinate of the user and the ship in the game.
    def move(pid, x, y):
        pass
