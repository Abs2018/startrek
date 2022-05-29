from subprocess import call
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


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
            elif command == "N" or command == "n":
                print("")
                art.cd(2, '', "Maybe next time...", 0, True)
                print("")
                quit()
        else:
            # Load player information
            print("We found you.")

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

        connection = db.stdb()
        query = "INSERT INTO `players` (`callsign`, `fname`, `mname`, `lname`, `alignment`, `rank`, `branch`, `xp`, `kills`, `deaths`, `locationx`, `locationy`, `whereami`, `health`, `species`, `age`, `birthday`, `homeplanet`, `languages`) VALUES ('"+str(callsign)+"', '"+str(fname)+"', '"+str(mname)+"', '"+str(
            lname)+"', '"+str(alignment)+"', '"+str(rank)+"', '"+str(branch)+"', '"+str(xp)+"', '"+str(kills)+"', '"+str(deaths)+"', '"+str(locationx)+"', '"+str(locationy)+"', '"+str(whereami)+"', '"+str(health)+"', '"+str(species)+"', '"+str(age)+"', '"+str(birthday)+"', '"+str(homeplanet)+"', '"+str(languages)+"')"
        db.query(connection, query)

    def load(callsign):
        pass

    def changexp(callsign, xp):
        pass
