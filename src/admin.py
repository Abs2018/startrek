# This is the admin app.

# Import the required modules.
from posixpath import split
from tracemalloc import start
import mysql.connector
from mysql.connector import Error
import os
from modules import db
from modules import art
from modules import setup
from modules import bigbang as bb
from classes import playerClass
from classes import shipClass
playerClass = playerClass.player()
shipClass = shipClass.shipClass()

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


def galaxyradius():
    connection = db.stdb()
    query = "SELECT * FROM `settings` WHERE `settingname`='galaxyradius'"
    # print(query)
    results = db.query(connection, query)
    if results:
        for row in results:
            galaxyradius = int(row['settingvalue'])
    else:
        galaxyradius = "Unable to get the galaxy's radius."
    # print(type(galaxyradius))
    return galaxyradius


def anyplayers():
    connection = db.stdb()
    query = "SELECT * FROM `players`"
    # print(query)
    results = db.query(connection, query)
    if results:
        playercount = len(results)
    else:
        playercount = "No players found."
    return playercount


def anyships():
    connection = db.stdb()
    query = "SELECT * FROM `ships`"
    # print(query)
    results = db.query(connection, query)
    if results:
        shipcount = len(results)
    else:
        shipcount = "No ships found."
    return shipcount


def anyempires():
    connection = db.stdb()
    query = "SELECT * FROM `empires`"
    # print(query)
    results = db.query(connection, query)
    if results:
        empirecount = len(results)
    else:
        empirecount = "No empires found."
    return empirecount


def adm_main_menu():
    print("")
    art.cd(226, '', "\t\t\tSTAR TREK GAME CONFIGURATION MENU", "", True)
    print("")
    menuitem = 0
    # Row 1
    art.cd(5, '', "<", "", False)
    art.cd('light_cyan', '', "B", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "The Big Bang\t", "", False)
    playercount = anyplayers()
    menuitem = menuitem + 1
    if type(playercount) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "U", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "User Editor\t\t", "", End)

    shipcount = anyships()
    menuitem = menuitem + 1
    if type(shipcount) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "S", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "Ship Editor\t\t", "", End)

    galrad = galaxyradius()
    menuitem = menuitem + 1
    if type(galrad) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "C", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "Sector Editor\t", "", End)
    # Row 2
    empirecount = anyempires()
    menuitem = menuitem + 1
    if type(empirecount) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "E", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "Empire Editor\t", "", End)
    galrad = galaxyradius()
    menuitem = menuitem + 1
    if type(galrad) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "G", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "Galaxy Browser\t", "", End)

    # Row ??
    print("")
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
            case ('c' | 'C'):
                # Sector viewer.
                sector_menu()
            case ('e' | 'E'):
                # Empire editor.
                empire_menu()
            case ('g' | 'G'):
                # Galaxy Viewer.
                galaxymenu()
            case ('s' | 'S'):
                # Ship viewer.
                ship_menu()
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


def empire_menu():
    command = ""
    while command != "q":
        if command == "":
            print("")
            art.cd(5, '', "[Empire Editor] ", '', False)
            art.cd('light_cyan', '',
                   "Which empire would you like to edit? ", 0, False)
            art.cd(226, '', "[?]", '', False)
            art.cd('light_cyan', '', ": ", 0, False)
            command = input(" ")

        match command:
            case ('q' | 'Q'):
                adm_main_menu()


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
                        morality = row['morality']
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
                            case ('j' | 'J'):
                                morality = playerClass.changemorality(pid)
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
                                art.cd(2, '', str(alignment), "", True)
                                # Morality
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "J", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Morality:\t\t", "", False)
                                art.cd(2, '', str(morality), "", True)
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


def ship_menu():

    def ship_sub_menu():
        print("")
        art.cd(226, '', "\t\t\tSHIP EDITOR OPTIONS", "", True)
        print("")
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "C", "", False)
        art.cd(5, '', "> ", "", False)
        art.cd(2, '', "Create a New Ship", "", True)
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "E", "", False)
        art.cd(5, '', "> ", "", False)
        art.cd(2, '', "Edit a Ship", "", True)
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "D", "", False)
        art.cd(5, '', "> ", "", False)
        art.cd(2, '', "Delete a Ship", "", True)

    command = ""
    while command != "q":
        if command == "":
            print("")
            art.cd(5, '', "[Ship Editor] ", '', False)
            art.cd('light_cyan', '',
                   "What would you like to do? ", 0, False)
            art.cd(226, '', "[?]", '', False)
            art.cd('light_cyan', '', ": ", 0, False)
            command = input(" ")

        match command:
            case ('?' | ''):
                ship_sub_menu()
                command = ""
            case ('c' | 'C'):
                shipClass.shipClassCreate()
                break
            case ('e' | 'E'):
                shipClass.shipClassesView()
                break
            case ('q' | 'Q'):
                adm_main_menu()
            case _:
                shipClass.shipClassView(command)


def sector_menu():
    command = ""
    while command != "q":
        if command == "":
            print("")
            art.cd(5, '', "[Sector Editor] ", '', False)
            art.cd('light_cyan', '',
                   "Which sector would you like to edit? ", 0, False)
            art.cd(226, '', "[?]", '', False)
            art.cd('light_cyan', '', ": ", 0, False)
            command = input(" ")

        match command:
            case ('q' | 'Q'):
                adm_main_menu()


def galaxymenu():
    # Ensure that the galaxy has been created. Else quit.
    galrad = galaxyradius()
    if type(galrad) != int:
        art.cd(1, '', " ", '', True)
        art.cd(1, '', "The galaxy has not been created yet.", 0, True)
        adm_main_menu()
    command = ""
    while command != "q":
        if command == "":
            # Get the starting coordinates to view the galaxy with.
            print("")
            art.cd(5, '', "[Galaxy Viewer] ", '', False)
            art.cd('light_cyan', '',
                   "Which sector do you want to view? ", 0, False)

            art.cd(2, '', "(", '', False)
            art.cd(226, '', "-"+str(galrad)+","+str(galrad), '', False)
            art.cd(2, '', " to ", '', False)
            art.cd(226, '', str(galrad-1)+",-"+str(galrad-1), '', False)
            art.cd(2, '', ") ", '', False)
            art.cd(226, '', "[?]", '', False)
            art.cd('light_cyan', '', ": ", 0, False)
            command = input(" ")

        match command:
            case ('?' | ""):
                print("Help")
                galaxymenu()
            case ('q' | 'Q'):
                adm_main_menu()
            case _:
                startingpoint = command.split(',')
                locationx = int(startingpoint[0].strip())
                locationy = int(startingpoint[1].strip())
                if locationx < galrad*-1 or locationx > galrad-1 or locationy < galrad*-1 or locationy > galrad:
                    print("")
                    art.cd(
                        1, '', "This number is beyond the edge of the galaxy. Try again.", 0, False)
                    print("")
                    galaxymenu()
                else:
                    galaxybrowser(startingpoint, galrad)
                    galaxymenu()


def galaxybrowser(startingpoint, galrad):

    os.system('cls' if os.name == 'nt' else 'clear')
    if startingpoint == "":
        locationx = 0
        locationy = 0
    else:
        locationx = int(startingpoint[0].strip())
        locationy = int(startingpoint[1].strip())
    # Calculate boundaries.
    edgeleft = locationx - 10
    edgeright = locationx + 11
    edgetop = locationy + 2
    edgebottom = locationy - 3
    # print("The center of the map is "+str(locationx)+", "+str(locationy))
    # print("The top left boundary is "+str(edgeleft)+", "+str(edgetop))
    # print("The top right boundary is "+str(edgeright)+", "+str(edgetop))
    # print("The bottom left boundary is "+str(edgeleft)+", "+str(edgebottom))
    # print("The bottom right boundary is "+str(edgeright)+", "+str(edgebottom))
    # * Start displaying the sensors
    # Row 1
    art.cd(2, '', "╔═══════════════════════════════════════════════════════╦═══════════════════════════════════════════════════════╗", "", True)

    def displayxaxis(edgeleft, edgeright, xposition, galrad):
        # Row 2-4: Display the X axis
        # Three arrays: xtop, xmid, xbot. They will hold the values for each column in this row.
        xtop = ["   "]
        xmid = ["   "]
        xbot = ["   "]
        for curx in range(edgeleft, edgeright):  # For pointer in range -10 - 11
            seclength = len(str(curx))  # Get the length of the pointer
            #! Because -100 shows strlen of 4.
            # print("")
            # print("Curx is: "+str(curx))
            # print("Before: "+str(seclength))
            if curx < 0 and curx >= -999:
                seclength = 3
            elif curx <= -1000 and curx >= -9999:
                seclength = 4
            elif curx <= -10000 and curx >= -99999:
                seclength = 5
            elif curx <= -100000 and curx >= -999999:
                seclength = 6
            elif curx <= -1000000 and curx >= -9999999:
                seclength = 7
            elif curx <= -10000000 and curx >= -99999999:
                seclength = 8
            elif curx <= -100000000 and curx >= -999999999:
                seclength = 9
            # print("After: "+str(seclength))

            match seclength:  # Match the length of the pointer.
                case seclength if seclength <= 3:  # From 0 - 999
                    # Since the length is 3, we will never have anything in the top or bottom rows and we append blanks to the list.
                    xtop.append("     ")
                    xbot.append("     ")
                    # If the number is less than -10 and less than 10:
                    if curx > -10 and curx < 10:
                        # If a negative number, convert it to positive.
                        if curx < 0:
                            curx = curx * -1
                        # Append the number to the list.
                        xmid.append("  "+str(curx)+"  ")
                    # If the number is between 10 and 99
                    elif curx >= 10 and curx < 100:  # Positive Formatter
                        # Append the number to the list.
                        xmid.append("  "+str(curx)+" ")
                    # If the number is between -10 and -99
                    elif curx > -100 and curx <= -10:  # Negative Formatter
                        # If a negative number, convert it to positive.
                        curx = curx * -1
                        # Append the number to the list.
                        xmid.append("  "+str(curx)+" ")
                    elif curx >= 100:  # Positive Formatter
                        # Append the number to the list.
                        xmid.append(" "+str(curx)+" ")
                    elif curx <= -100:  # Negative Formatter
                        # If a negative number, convert it to positive.
                        curx = curx * -1
                        # Append the number to the list.
                        xmid.append(" "+str(curx)+" ")
                    else:
                        print("Something went wrong. Quitting.")
                        quit()
                case seclength if seclength >= 4 and seclength <= 6:  # From 1000 - 999999
                    # Split cur x. Get the last three from the back and put it in the middle. Put the rest in the top row. The bottom stays empty.
                    if curx < 0:
                        curx = curx*-1
                    if seclength == 4:
                        # 1000
                        rowtop = str(curx)[0:1]
                        prefix = "   "
                        suffix = " "
                    elif seclength == 5:
                        # 10000
                        rowtop = str(curx)[0:2]
                        prefix = "  "
                        suffix = " "
                    elif seclength == 6:
                        # 100000
                        rowtop = str(curx)[0:3]
                        prefix = " "
                        suffix = " "
                    rowmid = str(curx)[-3:]
                    xtop.append(prefix+str(rowtop)+suffix)
                    xmid.append(" "+str(rowmid)+" ")
                    xbot.append("     ")
                case seclength if seclength >= 7 and seclength <= 9:  # From 1000000 - 999999999
                    # Split cur x. Get the last three from the back and put it in the middle. Put the rest in the top row. The bottom stays empty.
                    if curx < 0:
                        curx = curx*-1
                    if seclength == 7:
                        # 1 000 000
                        rowtop = str(curx)[0:1]
                        prefix = "   "
                        suffix = " "
                        rowmid = str(curx)[1:4]
                    elif seclength == 8:
                        # 10 000 000
                        rowtop = str(curx)[0:2]
                        prefix = "  "
                        suffix = " "
                        rowmid = str(curx)[2:5]
                    elif seclength == 9:
                        # 100 000 000
                        rowtop = str(curx)[0:3]
                        prefix = " "
                        suffix = " "
                        rowmid = str(curx)[3:6]
                    rowbot = str(curx)[-3:]
                    xtop.append(prefix+str(rowtop)+suffix)
                    xmid.append(" "+str(rowmid)+" ")
                    xbot.append(" "+str(rowbot)+" ")
                case _:
                    xtop.append(" RAD ")
                    xmid.append(" IAT ")
                    xbot.append(" ION ")
        xtop.append("   ")
        xmid.append("   ")
        xbot.append("   ")
        # Display the X Axis row.
        art.cd(2, '', "║", "", False)
        art.cd(2, '', str(xtop[0]), "", False)

        i = 1
        for curx in range(edgeleft, edgeright+1):
            if curx < 0 and xposition < 0:  # Alpha Quadrant
                art.cd(4, '', str(xtop[i]), "", False)
            elif curx > 0 and xposition < 0:  # Beta Quadrant
                art.cd(1, '', str(xtop[i]), "", False)
            elif curx > 0 and xposition > 0:  # Delta Quadrant
                art.cd(3, '', str(xtop[i]), "", False)
            elif curx < 0 and xposition > 0:  # Gamma Quadrant
                art.cd(5, '', str(xtop[i]), "", False)
            else:
                art.cd(15, '', str(xtop[i]), "", False)
            i = i+1
        art.cd(2, '', "║", "", True)
        art.cd(2, '', "║", "", False)
        art.cd(2, '', str(xmid[0]), "", False)
        i = 1
        for curx in range(edgeleft, edgeright+1):
            # print("")
            # print("Current X: "+str(curx))
            # print("Current I: "+str(i))

            if curx < 0 and xposition < 0:  # Alpha Quadrant
                art.cd(4, '', str(xmid[i]), "", False)
            elif curx > 0 and xposition < 0:  # Beta Quadrant
                art.cd(1, '', str(xmid[i]), "", False)
            elif curx > 0 and xposition > 0:  # Delta Quadrant
                art.cd(3, '', str(xmid[i]), "", False)
            elif curx < 0 and xposition > 0:  # Gamma Quadrant
                art.cd(5, '', str(xmid[i]), "", False)
            else:
                art.cd(15, '', str(xmid[i]), "", False)
            i = i+1
            # print("")
        art.cd(2, '', "║", "", True)
        art.cd(2, '', "║", "", False)
        art.cd(2, '', str(xbot[0]), "", False)
        i = 1
        for curx in range(edgeleft, edgeright+1):
            if curx < 0 and xposition < 0:  # Alpha Quadrant
                art.cd(4, '', str(xbot[i]), "", False)
            elif curx > 0 and xposition < 0:  # Beta Quadrant
                art.cd(1, '', str(xbot[i]), "", False)
            elif curx > 0 and xposition > 0:  # Delta Quadrant
                art.cd(3, '', str(xbot[i]), "", False)
            elif curx < 0 and xposition > 0:  # Gamma Quadrant
                art.cd(5, '', str(xbot[i]), "", False)
            else:
                art.cd(15, '', str(xbot[i]), "", False)
            i = i+1
        art.cd(2, '', "║", "", True)
        # END X AXIS DISPLAY

    displayxaxis(edgeleft, edgeright, edgetop, galrad)

    def displaycoordinate(axis, row, coordinate, edge, galrad):
        colorcoordinate = coordinate
        seclength = len(str(coordinate))  # Get the length of the pointer
        #! Because -100 shows strlen of 4.
        # print("")
        # print("Coordinate is: "+str(coordinate))
        # print("Sector Length Before: "+str(seclength))
        if coordinate < 0 and coordinate >= -999:
            seclength = 3
        elif coordinate <= -1000 and coordinate >= -9999:
            seclength = 4
        elif coordinate <= -10000 and coordinate >= -99999:
            seclength = 5
        elif coordinate <= -100000 and coordinate >= -999999:
            seclength = 6
        elif coordinate <= -1000000 and coordinate >= -9999999:
            seclength = 7
        elif coordinate <= -10000000 and coordinate >= -99999999:
            seclength = 8
        elif coordinate <= -100000000 and coordinate >= -999999999:
            seclength = 9
        # print("Sector Length After: "+str(seclength))
        match seclength:  # Match the length of the pointer.
            case seclength if seclength <= 3:  # From 0 - 999
                # Since the length is 3, we will never have anything in the top or bottom rows and we append blanks to the list.
                axistop = "   "
                axisbot = "   "
                # If the number is less than -10 and less than 10:
                if coordinate > -10 and coordinate < 10:
                    # If a negative number, convert it to positive.
                    if coordinate < 0:
                        coordinate = coordinate * -1
                    # Append the number to the list.
                    axismid = " "+str(coordinate)+" "
                # If the number is between 10 and 99
                elif coordinate >= 10 and coordinate < 100:  # Positive Formatter
                    # Append the number to the list.
                    axismid = " "+str(coordinate)
                # If the number is between -10 and -99
                elif coordinate > -100 and coordinate <= -10:  # Negative Formatter
                    # If a negative number, convert it to positive.
                    coordinate = coordinate * -1
                    # Append the number to the list.
                    axismid = " "+str(coordinate)
                elif coordinate >= 100:  # Positive Formatter
                    # Append the number to the list.
                    axismid = str(coordinate)
                elif coordinate <= -100:  # Negative Formatter
                    # If a negative number, convert it to positive.
                    coordinate = coordinate * -1
                    # Append the number to the list.
                    axismid = str(coordinate)
                else:
                    print("Unable to determine sector length. Quitting.")
                    quit()
            case seclength if seclength >= 4 and seclength <= 6:  # From 1000 - 999999
                # Split cur axis. Get the last three from the back and put it in the middle. Put the rest in the top row. The bottom stays empty.
                if coordinate < 0:
                    coordinate = coordinate*-1
                if seclength == 4:
                    # 1000
                    rowtop = str(coordinate)[0:1]
                    prefix = "  "
                    suffix = ""
                elif seclength == 5:
                    # 10000
                    rowtop = str(coordinate)[0:2]
                    prefix = " "
                    suffix = ""
                elif seclength == 6:
                    # 100000
                    rowtop = str(coordinate)[0:3]
                    prefix = ""
                    suffix = ""
                rowmid = str(coordinate)[-3:]
                axistop = prefix+str(rowtop)+suffix
                axismid = ""+str(rowmid)+""
                axisbot = "   "
            case seclength if seclength >= 7 and seclength <= 9:  # From 1000000 - 999999999
                # Split cur x. Get the last three from the back and put it in the middle. Put the rest in the top row. The bottom stays empty.
                if coordinate < 0:
                    coordinate = coordinate*-1
                if seclength == 7:
                    # 1 000 000
                    rowtop = str(coordinate)[0:1]
                    prefix = "  "
                    suffix = ""
                    rowmid = str(coordinate)[1:4]
                elif seclength == 8:
                    # 10 000 000
                    rowtop = str(coordinate)[0:2]
                    prefix = " "
                    suffix = ""
                    rowmid = str(coordinate)[2:5]
                elif seclength == 9:
                    # 100 000 000
                    rowtop = str(coordinate)[0:3]
                    prefix = ""
                    suffix = ""
                    rowmid = str(coordinate)[3:6]
                rowbot = str(coordinate)[-3:]
                axistop = prefix+str(rowtop)+suffix
                axismid = str(rowmid)
                axisbot = str(rowbot)
            case _:
                axistop = "ERR"
                axismid = "ERR"
                axisbot = "ERR"

        # Colour the text
        # If coord...then axistop = art.cd()

        if axis == "x":
            pass
        else:
            #! Try to show the Y coords on the right in the appropriate colour.
            if colorcoordinate < 0 and edge < 0:  # Alpha Quadrant
                if row == 0:
                    axistop = art.cd(4, '', str(axistop), "", False)
                elif row == 1:
                    axismid = art.cd(4, '', str(axismid), "", False)
                elif row == 2:
                    axisbot = art.cd(4, '', str(axisbot), "", False)
            elif colorcoordinate < 0 and edge > 0:  # Beta Quadrant
                if row == 0:
                    axistop = art.cd(1, '', str(axistop), "", False)
                elif row == 1:
                    axismid = art.cd(1, '', str(axismid), "", False)
                elif row == 2:
                    axisbot = art.cd(1, '', str(axisbot), "", False)
            elif colorcoordinate > 0 and edge > 0:  # Delta Quadrant
                if row == 0:
                    axistop = art.cd(3, '', str(axistop), "", False)
                elif row == 1:
                    axismid = art.cd(3, '', str(axismid), "", False)
                elif row == 2:
                    axisbot = art.cd(3, '', str(axisbot), "", False)
            elif colorcoordinate > 0 and edge < 0:  # Gamma Quadrant
                if row == 0:
                    axistop = art.cd(5, '', str(axistop), "", False)
                elif row == 1:
                    axismid = art.cd(5, '', str(axismid), "", False)
                elif row == 2:
                    axisbot = art.cd(5, '', str(axisbot), "", False)
            else:  # 0 axis
                if row == 0:
                    axistop = art.cd(15, '', str(axistop), "", False)
                elif row == 1:
                    axismid = art.cd(15, '', str(axismid), "", False)
                elif row == 2:
                    axisbot = art.cd(15, '', str(axisbot), "", False)
        # print(axistop)
        # print(axismid)
        # print(axisbot)

        # return [axistop, axismid, axisbot]

    def sensormid(locationx, locationy):
        connection = db.stdb()
        query = "SELECT `stars`.`sid`,`stars`.`scid`,`starclass`.`colour` FROM `starclass` " + \
            "INNER JOIN `stars` " + \
            "ON `stars`.`scid`=`starclass`.`scid` " + \
            "WHERE `stars`.`x` = '" + \
            str(locationx)+"' AND `stars`.`y` = '" + \
            str(locationy)+"'"
        # print(query)
        results = db.query(connection, query)
        if results:
            i = 1
            for row in results:
                if i <= 1:
                    if len(results) == 1:
                        colour = row['colour']
                        art.cd(colour, '', "•", "", False)
                    elif len(results) == 2:
                        colour = row['colour']
                        art.cd(colour, '', "⁚", "", False)
                    elif len(results) == 3:
                        colour = row['colour']
                        art.cd(colour, '', "⁖", "", False)
                    elif len(results) == 4:
                        colour = row['colour']
                        art.cd(colour, '', "⁛", "", False)
                    elif len(results) == 5:
                        colour = row['colour']
                        art.cd(colour, '', "⁙", "", False)
                    elif len(results) == 6:
                        colour = row['colour']
                        art.cd(colour, '', "⠿", "", False)
                    elif len(results) == 7:
                        colour = row['colour']
                        art.cd(colour, '', "፨", "", False)
                    else:
                        colour = row['colour']
                        art.cd(colour, '', "⁕", "", False)
                    i = i + 1
                else:
                    break

        else:
            art.cd(2, '', " ", "", False)

    def displaysensorrow(edgeleft, edgeright, edgetop, edgebottom, galrad):
        # This is a marker for the Y axis to determine where we are in the column.
        y = 0
        # This is a marker to determine which position in the row we are in (eg: top (0), middle (1), or bottom (2))
        position = 0
        # For every row of displayable data
        for cury in range(edgetop, edgebottom, -1):
            while position < 3:
                x = 0
                # Go through the columns and display the data
                xcursor = 0
                for curx in range(edgeleft, edgeright+2):
                    # This is a marker for the X axis to determine where we are in the row.
                    # If the first column, display the sector name
                    if x == 0:
                        if y == 2 and position == 1:
                            art.cd(2, '', "╠", "", False)
                        else:
                            art.cd(2, '', "║", "", False)
                        # In each Sensor Row exists a top, middle, and bottom row.
                        coordnumber = displaycoordinate(
                            'y', position, cury, edgeleft, galrad)
                        # art.cd(4, '', " ", "", False)
                        # art.cd(4, '', str(cury), "", False)
                        # art.cd(4, '', " ", "", False)
                    # If the last column, dispay the sector name
                    elif x == 22:
                        coordnumber = displaycoordinate(
                            'y', position, cury, edgeright-1, galrad)

                        # coordnumber[position]
                        # art.cd(4, '', " ", "", False)
                        # art.cd(4, '', str(cury), "", False)
                        # art.cd(4, '', " ", "", False)
                        if y == 2 and position == 1:
                            art.cd(2, '', "╣", "", True)
                        else:
                            art.cd(2, '', "║", "", True)
                    # Otherwise, display the sector information.
                    else:
                        if position == 0:  # * TOP
                            # Should we decide to indicate other top sector features, they will be displayed here.
                            if y == 2 and xcursor == 11:
                                art.cd(172, '', "  ┬  ", 0, False)
                            elif (cury > galrad and edgetop > galrad and cury > 0) or (cury <= galrad*-1 and edgebottom < 0):
                                art.cd(2, '', " RAD ", 0, False)
                            elif curx > galrad or curx < (galrad*-1)+1:
                                art.cd(2, '', " RAD ", 0, False)
                            else:
                                art.cd(4, '', "     ", "", False)
                        elif position == 1:  # * MIDDLE
                            # Display stars here.
                            if y == 2 and xcursor == 11:
                                art.cd(172, '', "├ ", 0, False)
                                sensormid(curx-1, cury)
                                art.cd(172, '', " ┤", 0, False)
                            elif (cury > galrad and edgetop > galrad and cury > 0) or (cury <= galrad*-1 and edgebottom < 0):
                                art.cd(2, '', " IAT ", 0, False)
                            elif curx > galrad or curx < (galrad*-1)+1:
                                art.cd(2, '', " IAT ", 0, False)
                            else:  # * BOTTOM
                                art.cd(172, '', "  ", 0, False)
                                sensormid(curx-1, cury)
                                art.cd(172, '', "  ", 0, False)
                        elif position == 2:
                            # Should we decide to indicate other bottom sector features, they will be displayed here.
                            if y == 2 and xcursor == 11:
                                art.cd(172, '', "  ┴  ", 0, False)
                            elif (cury > galrad and edgetop > galrad and cury > 0) or (cury <= galrad*-1 and edgebottom < 0):
                                art.cd(2, '', " ION ", 0, False)
                            elif curx > galrad or curx < (galrad*-1)+1:
                                art.cd(2, '', " ION ", 0, False)
                            else:
                                art.cd(4, '', "     ", "", False)
                        else:
                            art.cd(2, '', "ERROR", "", False)
                    x = x+1
                    xcursor = xcursor + 1
                # Move on to the next row.
                if position == 2:
                    position = 0
                    break
                else:
                    position = position + 1
            y = y+1

        #! YOU NEED TO PUT THE Y COUNTER IN THE range of 3. It should only increment after the bottom row has gone up.

    displaysensorrow(edgeleft, edgeright, edgetop, edgebottom, galrad)

    displayxaxis(edgeleft, edgeright, edgebottom+1, galrad)
    # * Sensor Information Bar
    art.cd(2, '', "╠═══════════════════════════════════════════════════════╩═══════════════════════════════════════════════════════╣", "", True)
    art.cd(2, '', "║                                                                                                               ║", "", True)

    # * End the sensor window
    art.cd(2, '', "╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝", "", True)

    '''
    By default, the console size is 120x30, subtract 1 for the command prompt, one for the sector information above the command prompt, and two more for the frames on either side, the viewable space is 118x26. Subtract 3 on the left and top for coordinates and we are left with a viewable space of 115x22. We will also shave three off the right side so that we can have an odd number of sectors on the X axis and show the center cursor, so we end up with 

    sectors will appear in columns of 3:
╔═══════════════════════════════════════════════════════╦════════════════════════════════════════════════════╗
║                                                                                          10       100  100 ║
║     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   ...  000  ...  000  000 ║
║                                                                                                   000  001 ║
║                                                                                                            ║
║ 1   *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *  ║   
║                                                                                                            ║
║                                                                                                            ║
║                                                                                                            ║
║ 2   *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *  ║
║                                                                                                            ║
║                                                                                                            ║
║ 10                                             Ports:0┬1:Planets                                           ║
╠000  *    .    .    *    *    .    .    *    *    .  ├ • ┤  *    *    .    .    *    *    .    .    *    *  ║
║                                                Ships:2┴0:Mines                                             ║
║                                                                                                            ║
║100                                                                                                         ║
║000  *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *  ║
║000                                                                                                         ║
║                                                                                                            ║
║                                                                                                            ║
║100                                                                                                         ║
║000  *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *    .    .    *    *  ║
║000                                                                                                         ║
║                                                                                                            ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║ [11,10000] Federation Space, Star Name                                                                     ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

Command Prompt (?): 
    
    
    What happens at the edge of the galaxy? Don't move part the outer edge. The 
    What happens if the galaxy is smaller than 110 sectors? Center in on 0,0 and draw the numbers that exist.

    The square brackets denote the current location of the user.

    Characters from https://en.wikipedia.org/wiki/Code_page_437

    ░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
    · ∙ ° ° • . * 



    '''


# The Main Menu
adm_main_menu()
