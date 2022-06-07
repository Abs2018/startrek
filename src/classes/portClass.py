from datetime import datetime
from classes import log
import math
from dataclasses import dataclass
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
from classes import playerClass
playerClass = playerClass.player()
log = log.log()
# TODO:
#! BUG: Because you calculate months as 30 days, it is possible to get output like this at a port: Alex Tiberius Kurt docked here 5 years 2 months -23 days 1 hour and 31 minutes ago.


@dataclass
class portClass():
    def __init__(self):
        pass

    '''
    This function returns all the attributes of the specific port class. Used primarily in what port menu options to display.
    '''

    def portAttributes(self, portclass):
        connection = db.stdb()
        query = "select * from `portclass` where `portclass` = '" + \
                str(portclass)+"'"
        # print(query)
        results = db.query(connection, query)
        if results:
            for row in results:
                pcid = row['pcid']
                portclass = row['portclass']
                orecap = row['orecap']
                organicscap = row['organicscap']
                equipmentcap = row['equipmentcap']
                theater = row['theater']
                bank = row['bank']
                techdealer = row['techdealer']
                police = row['police']
                shipyards = row['shipyards']
                tavern = row['tavern']
                bar = row['bar']
                library = row['library']
                blackmarket = row['blackmarket']
                description = row['description']
            portattributes = {"pcid": pcid, "portclass": portclass, "orecap": orecap, "organicscap": organicscap, "equipmentcap": equipmentcap, "theater": theater,
                              "bank": bank, "techdealer": techdealer, "police": police, "shipyards": shipyards, "tavern": tavern, "bar": bar, "library": library, "blackmarket": blackmarket, "description": description}
            return portattributes
        else:
            print("")
            art.cd(9, '', "Could not load the port class. Quitting.")
            print("")
            quit()

    def portDock(self, playerinfo):
        # Check if there is a port in this sector. If not, show error message.
        connection = db.stdb()
        query = "SELECT * FROM `ports` WHERE `locationx` = '" + \
                str(playerinfo.locationx)+"' AND `locationy` = '" + \
            str(playerinfo.locationy)+"'"
        # print(query)
        results = db.query(connection, query)
        if results:
            # Get Port Class
            thisportclass = portClass.portGetClass(
                playerinfo.locationx, playerinfo.locationy)
            portname = portClass.portGetName(
                playerinfo.locationx, playerinfo.locationy)
            # Show animation of port landing.
            match thisportclass:
                case 0:
                    art.portAnimClass0(portname)

            # Update player location
            playerinfo.whereami = playerClass.changewhereami(
                playerinfo.pid, "port")

            # Get the port ID (portid)
            connection = db.stdb()
            query = "SELECT `portid` FROM `ports` WHERE `locationx` = '" + \
                str(playerinfo.locationx)+"' AND `locationy` = '" + \
                str(playerinfo.locationy)+"'"
            results = db.query(connection, query)
            if results:
                for row in results:
                    portid = row['portid']
            # Start printing the docking log.
            art.cd(11, '', "Activity report for ", 0, False)
            art.cd(14, '', portname, 0, False)
            art.cd(11, '', ": TIMESTAMP PLACEHOLDER", 0, True)
            art.cd(13, "", "-=-=-        Docking Log        -=-=-", 0, True)
            # Get the last time and date that someone docked here, and assign XP as desired.
            connection = db.stdb()
            query = "SELECT `pid`,`lastdockeddate` FROM `portlastdocked` WHERE `portid` = '" + \
                str(portid)+"' ORDER BY `ldapid` DESC LIMIT 1"
            # print(query)
            results = db.query(connection, query)

            def dockedtimedelta(lastdockeddate):
                # Get the number of days it has been since someone docked
                timenow = datetime.now()
                lasttockedday = str(timenow-lastdockeddate)
                lasttockedday = lasttockedday.split(" ")
                return lasttockedday
            if results:  # Someone has docked in the past.
                for row in results:
                    lastdockedpid = row['pid']
                    lastdockeddate = row['lastdockeddate']
                # Get the Name of who docked last
                connection = db.stdb()
                query = "SELECT `fname`,`mname`,`lname` FROM `players` WHERE `pid` = '" + \
                    str(lastdockedpid)+"'"
                results = db.query(connection, query)
                if results:
                    for row in results:
                        fname = row['fname']
                        mname = row['mname']
                        lname = row['lname']
                if mname == "":
                    playername = str(fname)+" "+str(lname)
                else:
                    playername = str(fname)+" "+str(mname)+" "+str(lname)
                # Date calculations
                lastdockeddate = dockedtimedelta(lastdockeddate)
                # print(lastdockeddate)
                # ???????????????????????????? This is the dataset.
                # ['0:00:11.123315']
                # ['1', 'day,', '0:03:05.069710']
                # ['366', 'days,', '0:04:28.446557']
                # ['3284', 'days,', '0:05:01.983308']
                datelistsize = len(lastdockeddate)
                year = 0
                month = 0
                day = 0
                hour = 0
                minute = 0
                second = 0
                match datelistsize:
                    case 1:
                        # Hours
                        lastdocked = lastdockeddate[0].split(".")
                        lastdocked = lastdocked[0].split(":")
                        # Trim leading zeroes and determine plurality
                        if len(lastdocked[0]) > 1:
                            if lastdocked[0][0] == '0':
                                lastdocked[0] = lastdocked[0][1:]
                        if int(lastdocked[0]) == 1:
                            hour = " hour"
                        else:
                            hour = " hours"
                        if len(lastdocked[1]) > 1:
                            if lastdocked[1][0] == '0':
                                lastdocked[1] = lastdocked[1][1:]
                        if int(lastdocked[1]) == 1:
                            minute = " minute"
                        else:
                            minute = " minutes"
                        if len(lastdocked[2]) > 1:
                            if lastdocked[2][0] == '0':
                                lastdocked[2] = lastdocked[2][1:]
                        if int(lastdocked[2]) == 1:
                            second = " second"
                        else:
                            second = " seconds"
                        # Create list
                        lastdocked = [0, year, 0, month, 0, day, lastdocked[0], hour,
                                      lastdocked[1], minute, lastdocked[2], second]
                        # Calculate XP
                        xp = 0
                    case 3:
                        # Days
                        # print(lastdockeddate)
                        lastdocked = lastdockeddate[2].split(".")
                        lastdocked = lastdocked[0].split(":")
                        lastdocked = [lastdockeddate[0],
                                      lastdockeddate[1], lastdocked[0], lastdocked[1], lastdocked[2]]
                        # Calculate XP. If no one for 14 days, give 2 points, otherwise, give an additional point for every subsequent day.
                        if int(lastdockeddate[0]) <= 14:
                            xp = 0
                        else:
                            xp = (int(lastdockeddate[0]) + 2) - 14
                        if int(xp) > 50:
                            xp = 50

                        # Hours, minutes, and seconds
                        if len(lastdocked[4]) > 1:
                            if lastdocked[4][0] == '0':
                                lastdocked[4] = lastdocked[4][1:]
                        if int(lastdocked[4]) == 1:
                            second = " second"
                        else:
                            second = " seconds"
                        seconds = lastdocked[4]
                        if len(lastdocked[3]) > 1:
                            if lastdocked[3][0] == '0':
                                lastdocked[3] = lastdocked[3][1:]
                        if int(lastdocked[3]) == 1:
                            minute = " minute"
                        else:
                            minute = " minutes"
                        minutes = lastdocked[3]
                        if len(lastdocked[2]) > 1:
                            if lastdocked[2][0] == '0':
                                lastdocked[2] = lastdocked[2][1:]
                        if int(lastdocked[2]) == 1:
                            hour = " hour"
                        else:
                            hour = " hours"
                        hours = lastdocked[2]
                        # This is the word day/days. The function states this correctly.
                        day = " "+lastdocked[1]
                        # Days, months, years
                        if int(lastdocked[0]) > 364:  # Years is true
                            if int(lastdocked[0]) >= 730:
                                year = " years"
                            else:
                                year = " year"
                            # Calculate the number of years.
                            years = int(lastdocked[0])/365
                            years = int(math.floor(years))
                        if int(lastdocked[0]) > 30:  # Months is true
                            # Calculate the number of months.
                            months = int(lastdocked[0])/30
                            months = int(months) % 12
                            months = int(math.floor(months))
                            if int(months) == 1:
                                month = " month"
                            else:
                                month = " months"
                        # Calculate remaining days.
                        days = int(lastdocked[0]) - \
                            (int(years)*365)-(int(months)*30)
                        if days == 1:
                            day = " day"
                        else:
                            day = " days"

                        # Create list
                        lastdocked = [years, year, months, month, days, day, hours, hour,
                                      minutes, minute, seconds, second]

                # If someone has docked before:
                art.cd(14, "", str(playername), 0, False)
                art.cd(2, "", " docked here", 0, False)

                # ['1', 'day,', '0:03:05.069710']
                # ['366', 'days,', '0:04:28.446557']
                # ['3284', 'days,', '0:05:01.983308']
                # print(lastdocked)
                # [0, 0, 0, 0, 0, 0, '0', 0, '58', ' minutes', '43', ' seconds']
                if int(lastdocked[0]) != 0:  # Years
                    art.cd(14, '', " " + str(lastdocked[0]), 0, False)
                    art.cd(2, '', str(lastdocked[1]), 0, False)
                if int(lastdocked[2]) != 0:  # Months
                    art.cd(14, '', " " + str(lastdocked[2]), 0, False)
                    art.cd(2, '', str(lastdocked[3]), 0, False)
                if int(lastdocked[4]) != 0:  # Days
                    art.cd(14, '', " " + str(lastdocked[4]), 0, False)
                    art.cd(2, '', str(lastdocked[5]), 0, False)
                if int(lastdocked[6]) != 0:  # Hours
                    art.cd(14, '', " " + str(lastdocked[6]), 0, False)
                    art.cd(2, '', str(lastdocked[7]), 0, False)
                if int(lastdocked[8]) != 0:  # Minutes
                    if int(lastdocked[6]) != 0 or int(lastdocked[4]) != 0:
                        art.cd(2, '', " and", 0, False)
                    art.cd(14, '', " " + str(lastdocked[8]), 0, False)
                    art.cd(2, '', str(lastdocked[9]), 0, False)
                if lastdocked[5] == 0:  # Seconds
                    if lastdocked[10] != 0:
                        art.cd(14, '', " " + str(lastdocked[10]), 0, False)
                        art.cd(2, '', str(lastdocked[11]), 0, False)
                art.cd(2, "", " ago.", 0, True)
                # Show XP Message, if last docked date is greater than 14 days.
                # xp = lastdockeddate[0]
                if int(xp) >= 14:
                    # Print the amount of XP that is being awarded.
                    art.cd(
                        2, '', "For being the first visitor in a while, you receive ", 0, False)
                    art.cd(11, '', str(xp), 0, False)
                    art.cd(2, '', " experience points.", 0, False)
            else:  # No one has docked here before.
                # If no one has docked check to see how long the game has been running by getting portid=1.createdate.
                connection = db.stdb()
                query = "SELECT `createdate` FROM `ports` WHERE `portid` = '1'"
                results = db.query(connection, query)
                if results:
                    for row in results:
                        lastdockeddate = row['createdate']
                art.cd(2, "", "No current ship docking log on file.", 0, True)
                lastdockeddate = dockedtimedelta(lastdockeddate)
                # Calculate XP
                xp = lastdockeddate[0]
                if int(xp) > 50:
                    xp = 50
                elif int(xp) == 0:
                    # ! This is meant to give 1 xp point if the server is less than 24 hours old. However, what happens if the result of timedelta doesn't give the days as '0' when run?
                    # * This is meant to give 1 xp point if the server is less than 24 hours old. However, what happens if the result of timedelta doesn't give the days as '0' when run?
                    # ? This is meant to give 1 xp point if the server is less than 24 hours old. However, what happens if the result of timedelta doesn't give the days as '0' when run? Delete the galaxy and try again.
                    xp = 1
                art.cd(2, '', "For finding this unused port, you receive ", 0, False)
                art.cd(11, '', xp, 0, False)
                art.cd(2, '', " experience ", 0, False)
                if int(xp) == 1:
                    art.cd(2, '', "point.", 0, True)
                else:
                    art.cd(2, '', "points.", 0, True)

            # Give the user their XP
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! START HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # Update port last docked time. Always an INSERT to keep track of port activity.
            connection = db.stdb()
            query = "INSERT INTO `portlastdocked` (`portid`,`pid`)  VALUES ('" + \
                str(portid)+"','"+str(playerinfo.pid)+"')"
            # print(query)
            results = db.query(connection, query)

        else:
            art.cd(9, 0, "There is no port in this sector, sir.", 0, True)

    def portGetClass(locationx, locationy):
        connection = db.stdb()
        query = "SELECT `portclass` FROM `ports` WHERE `locationx` = '" + \
            str(locationx)+"' AND `locationy` = '" + \
            str(locationy)+"'"
        # print(query)
        results = db.query(connection, query)
        if results:
            for row in results:
                portclass = row['portclass']
        return portclass

    def portGetName(locationx, locationy):
        connection = db.stdb()
        query = "SELECT `portname` FROM `ports` WHERE `locationx` = '" + \
            str(locationx)+"' AND `locationy` = '" + \
            str(locationy)+"'"
        # print(query)
        results = db.query(connection, query)
        if results:
            for row in results:
                portname = row['portname']
        return portname
