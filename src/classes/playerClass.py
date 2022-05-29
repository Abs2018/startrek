from dataclasses import dataclass
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
from classes import log
log = log.log()

# TODO:
# * Check to make sure that the user's first name is not 'q'


@dataclass
class player():
    def __init__(self):
        pass

    def check(self):
        # Get the player name.
        art.cd(5, '', "", '', False)
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
        print("")
        art.cd(
            'cyan', '', "Give me a moment to sign you in...Okay, you're all set!", '', True)
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
        db.query(connection, query)
        # Log the event
        connection = db.stdb()
        logtype = "NEWPLAYER"
        logevent = fname + " " + lname + " joined the " + alignment + "!"
        log.logAdd(logtype, logevent)

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

    def changealignment(pid):
        pass

    def changerank(pid):
        pass

    def changebranch(pid):
        pass

    def changexp(pid, xp):
        # playerClass.changerank(pid)
        pass

    def changekills(pid):
        pass

    def changedeaths(pid):
        pass

    # This changes the X coordinate from the user editor.
    def changelocationx(pid, x):
        pass

    # This changes the y coordinate from the user editor.
    def changelocationy(pid, y):
        pass

    def changewhereami(pid, destination):
        pass

    def changehealth(pid, health):
        pass

    def changespecies(pid):
        pass

    def changeage(pid):
        pass

    def changebirthday(pid):
        pass

    def changehomeplanet(pid):
        pass

    def changelanguage(pid):
        pass

    # This changes the coordinate of the user and the ship in the game.
    def move(pid, x, y):
        pass
