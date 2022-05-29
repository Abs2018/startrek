# This is the admin app.

# Import the required modules.
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
from modules import setup
from modules import bigbang as bb
from classes import playerClass
playerClass = playerClass.player()


# import cgi


connection = db.stdb()
if connection == "FALSE":
    # The database has not been installed. Display setup menu.
    art.cd(22, '', "First time setup detected.", "reset", True)
    setup.setup()

# Continue to menu.
'''
Characters from https://en.wikipedia.org/wiki/Code_page_437

░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
· ∙ ° ° • . *

┌─┬─┐
│ │ │
├─┼─┤
└─┴─┘
'''


def adm_main_menu():
    print("")
    art.cd(226, '', "\t\t\tSTAR TREK GAME CONFIGURATION MENU", "", True)
    print("")
    # Row 1
    art.cd(5, '', "<", "", False)
    art.cd('light_cyan', '', "B", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "The Big Bang", "", False)

    art.cd(5, '', "\t<", "", False)
    art.cd('light_cyan', '', "S", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "Sector Editor", "", False)

    art.cd(5, '', "\t<", "", False)
    art.cd('light_cyan', '', "U", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "User Editor", "", True)

    # Row ??
    print("")
    art.cd(5, '', "<", "", False)
    art.cd('226', '', "Q", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "Quit Editor", "", True)
    # Footer
    art.cd("", "", "", "reset", True)

    command = ""
    while command != "q":
        art.cd('light_cyan', '', "Enter your choice ", 'reset', False)
        art.cd('226', '', "[?]", 'reset', False)
        art.cd('light_cyan', '', ": ", 'reset', False)
        command = input("")
        match command:
            case ('b' | 'B'):
                # The Big Bang
                bb.bb_main_menu()
                # This will display the menu once you leave the Big Bang Editor.
                adm_main_menu()
            case ('s' | 'S'):
                # Sector viewer.
                pass
            case ('u' | 'U'):
                # User viewer.
                user_menu()
            case ('?' | ''):
                adm_main_menu()
            case ('q' | 'Q'):
                print("")
                art.cd(0, 196, "  Live long and prosper  ", 'reset', True)
                print("")
                quit()
            case _:
                art.cd(1, '', 'Command not found. Please try again.',
                       "reset", True)
                print("")


def user_menu():
    command = ""
    while command != "q":
        if command == "":
            print("")
            art.cd(5, '', "[User Editor] ", '', False)
            art.cd('light_cyan', '',
                   "Which user would you like to edit? ", 0, False)
            art.cd(226, '', "[?]", '', False)
            art.cd('light_cyan', '', ": ", 0, False)
            command = input(" ")

        match command:
            case ('?' | ''):
                # Display all users
                connection = db.stdb()
                query = "select * from `players`"
                results = db.query(connection, query)

                print("")
                art.cd(226, '', "\t\t\tDISPLAYING ALL USERS", "", True)
                print("")
                for row in results:
                    art.cd(5, '', "<", "", False)
                    art.cd('light_cyan', '', str(row['pid']), "", False)
                    art.cd(5, '', "> ", "", False)
                    art.cd(2, '', row['fname'] + " " + row['lname'], "", True)
                command = ""
            case ('q' | 'Q'):
                adm_main_menu()
            case _:
                # Get the user's information
                connection = db.stdb()
                query = "select * from `players` where `pid`='"+command+"'"
                results = db.query(connection, query)
                if results:
                    for row in results:
                        pid = row['pid']
                        callsign = row['callsign']
                        fname = row['fname']
                        mname = row['mname']
                        lname = row['lname']
                        alignment = row['alignment']
                        rank = row['rank']
                        branch = row['branch']
                        xp = row['xp']
                        kills = row['kills']
                        deaths = row['deaths']
                        locationx = row['locationx']
                        locationy = row['locationy']
                        whereami = row['whereami']
                        health = row['health']
                        species = row['species']
                        age = row['age']
                        birthday = row['birthday']
                        homeplanet = row['homeplanet']
                        languages = row['languages']

                    usercommand = ""
                    while usercommand != "q" or usercommand != "Q":
                        match usercommand:
                            case ('c' | 'C'):
                                callsign = playerClass.changecallsign(pid)
                            case ('f' | 'F'):
                                fname = playerClass.changefname(pid)
                            case ('m' | 'M'):
                                mname = playerClass.changemname(pid)
                            case ('l' | 'L'):
                                lname = playerClass.changelname(pid)
                            case ('a' | 'A'):
                                alignment = playerClass.changealignment(pid)
                            case ('r' | 'R'):
                                rank = playerClass.changerank(pid)
                            case ('b' | 'B'):
                                branch = playerClass.changebranch(pid)
                            case ('e' | 'E'):
                                xp = playerClass.changexp(pid)
                            case ('k' | 'K'):
                                kills = playerClass.changekills(pid)
                            case ('d' | 'D'):
                                deaths = playerClass.changedeaths(pid)
                            case ('x' | 'X'):
                                locationx = playerClass.changelocationx(pid)
                            case ('y' | 'Y'):
                                locationy = playerClass.changelocationy(pid)
                            case ('w' | 'W'):
                                whereami = playerClass.changewhereami(
                                    pid)
                            case ('h' | 'H'):
                                health = playerClass.changehealth(pid)
                            case ('s' | 'S'):
                                species = playerClass.changespecies(pid)
                            case ('g' | 'G'):
                                age = playerClass.changeage(pid)
                            case ('i' | 'I'):
                                birthday = playerClass.changebirthday(pid)
                            case ('p' | 'P'):
                                homeplanet = playerClass.changehomeplanet(pid)
                            case ('n' | 'N'):
                                languages = playerClass.changelanguage(pid)
                            case ('q' | 'Q'):
                                adm_main_menu()
                            case ('?' | ''):
                                print("")
                                art.cd(
                                    226, '', "\t\t\tEDIT USER INFORMATION", "", True)
                                print("")
                                # Call Sign
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "C", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Callsign:\t\t", "", False)
                                art.cd(2, '', callsign, "", True)
                                # First Name
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "F", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "First Name:\t\t", "", False)
                                art.cd(2, '', fname, "", True)
                                # Middle Name
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "M", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Middle Name:\t", "", False)
                                art.cd(2, '', mname, "", True)
                                # Last Name
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "L", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Last Name:\t\t", "", False)
                                art.cd(2, '', lname, "", True)
                                # Alignment
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "A", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Alignment:\t\t", "", False)
                                art.cd(2, '', alignment, "", True)
                                # Rank
                                #! Do we need Rank? Can't we just calculate it from XP?
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "R", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Rank:\t\t", "", False)
                                art.cd(2, '', str(rank), "", True)
                                # Branch
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "B", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Branch:\t\t", "", False)
                                art.cd(2, '', branch, "", True)
                                # Experience (XP)
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "E", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Experience:\t\t", "", False)
                                art.cd(2, '', str(xp), "", True)
                                # Kills
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "K", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Kills:\t\t", "", False)
                                art.cd(2, '', str(kills), "", True)
                                # Deaths
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "D", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Deaths:\t\t", "", False)
                                art.cd(2, '', str(deaths), "", True)
                                # Location X
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "X", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "X Coordinate:\t", "", False)
                                art.cd(2, '', str(locationx), "", True)
                                # Location Y
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "Y", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Y Coordinate:\t", "", False)
                                art.cd(2, '', str(locationy), "", True)
                                # Where Am I?
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "W", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Where Am I?:\t", "", False)
                                art.cd(2, '', str(whereami), "", True)
                                # Health
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "H", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Health:\t\t", "", False)
                                art.cd(2, '', str(health), "", True)
                                # Species
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "S", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Species:\t\t", "", False)
                                art.cd(2, '', str(species), "", True)
                                # Age
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "G", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Age:\t\t", "", False)
                                art.cd(2, '', str(age), "", True)
                                # Birthday
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "I", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Birthday:\t\t", "", False)
                                art.cd(2, '', str(birthday), "", True)
                                # Home Planet
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "P", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Home Planet:\t", "", False)
                                art.cd(2, '', str(homeplanet), "", True)
                                # Language
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "N", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Language:\t\t", "", False)
                                art.cd(2, '', str(languages), "", True)
                                print()
                                art.cd(5, '', "<", "", False)
                                art.cd('226', '', "Q", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd(2, '', "Quit User Editor", "", True)
                                print()
                            case _:
                                print("")
                                art.cd(
                                    1, '', "Command not found. Please try again.", 0, True)
                                print("")

                        print("")
                        art.cd(5, '', "[User Editor] ", '', False)
                        art.cd('light_cyan', '',
                               "Which attribute would you like to edit? ", 0, False)
                        art.cd(226, '', "[?]", '', False)
                        art.cd('light_cyan', '', ": ", 0, False)
                        usercommand = input("")

                else:
                    print("")
                    art.cd(1, '', "User not found", '', True)
                    command = ""


# The Main Menu
adm_main_menu()
