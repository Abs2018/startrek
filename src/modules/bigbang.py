# The Big Bang! This will create the game world.
import math
import random
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art

# TODO
# * Right now planets are inhabited randomly, no matter the class. Focus on specific planet classes (Class M, etc) that are more likely to support life.
# * Need to add planet development stage for prime directive bonuses/penalties.
# * Add an algorithm for nebulas that may impact sensor performance.
# * Create black holes.
# * Determine if we want to keep port names on randomly generated trading ports.
# ! BUG: Despite popping the value of 0, there are many class 0 ports being created.
# * Add empires: there are the organizations that rule over planets.
#     * Create Class 0 ports in the empire. No more than 3 per empire.
# * Add predefined Federation empire.


def bb_main_menu():
    def bbmenu(sectors, roguechance, stars, planets, civilizations, ports, empires):
        print("")
        art.cd(226, '', "\tTHE BIG BANG", "", True)
        print("")

        connection = db.stdb()
        query = "select * from `stars` LIMIT 1"
        results = db.rowcount(connection, query)
        if results != 0:
            art.cd(5, '', "\t<", "", False)
            art.cd('81', '', "C", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(196, '', "Delete Galaxy", "", True)
            print("")

            # Row ??
            art.cd(5, '', "\t<", "", False)
            art.cd('226', '', "Q", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(2, '', "Return to previous menu", "", True)
            # Footer
            art.cd("", "", "", "reset", True)
        else:
            # Row 1
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "1", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "Approximately how many sectors should exist in the galaxy? ", "", False)
            art.cd(226, '', str(sectors), "", True)

            # Row 2
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "2", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "What chance is there that an empty sector will have a rogue planet? ", "", False)
            art.cd(226, '', str(roguechance), "", False)
            art.cd(226, '', "%", "", True)

            # Row 3
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "3", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "What chance is there of a star forming in a sector? ", "", False)
            art.cd(226, '', str(stars), "", False)
            art.cd(226, '', "%", "", True)

            # Row 4
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "4", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "What chance is there that there will be planets around a star? ", "", False)
            art.cd(226, '', str(planets), "", False)
            art.cd(226, '', "%", "", True)

            # Row 5
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "5", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "What chance is there of a planet being inhabited? ", "", False)
            art.cd(226, '', str(civilizations), "", False)
            art.cd(226, '', "%", "", True)

            # Row 6
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "6", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "What chance is there of a port being in the sector? ", "", False)
            art.cd(226, '', str(ports), "", False)
            art.cd(226, '', "%", "", True)

            # Row 7
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "7", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(2, '', "How many empires should be created? ", "", False)
            art.cd(226, '', str(empires), "", True)

            # Row 8
            print("")
            art.cd(5, '', "\t<", "", False)
            art.cd('81', '', "C", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(6, '', "Create the galaxy!", "", True)
            print("")

            # Row ??
            art.cd(5, '', "\t<", "", False)
            art.cd('226', '', "Q", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(2, '', "Return to previous menu", "", True)
            # Footer
            art.cd("", "", "", "reset", True)

    def bigbang(sectors, roguechance, stars, planets, civilizations, ports, empires):
        #!!!! Whatever changes you make in the bigbang function, please add the opposite in the bigdark function.
        # Do the math around the sector coordinates. Our galaxies will be a square grid.

        # We add one to account for the 0,0 coordinates.
        diameter = int(math.sqrt(int(sectors)))+1
        # Total area of the galaxy equals length * width
        totalsectors = diameter * diameter
        # print("The galaxy will be "+str(diameter) +" sectors wide and tall for a total of "+str(totalsectors)+".")
        radius = math.floor(diameter/2)
        x = radius*-1
        y = radius
        # print(x)
        # print(y)

        # * Create counters
        sectorcount = 0  # Total number of sectors tracker
        xdiametercount = 0  # Current X coordinate pointer
        ydiametercount = 0  # Current Y coordinate pointer
        starcount = 0  # Total number of stars created in the galaxy
        planetcount = 0  # Total number of planets created in the galaxy
        civcounter = 0  # Total number of civilizations created in the galaxy
        portcounter = 0  # Total number of civilizations created in the galaxy
        rogueplanets = []  # The rogue planet data for the executemany SQL function
        allstars = []  # The star data for the executemany SQL function
        planetswithstars = []  # The planet data for the executemany SQL function
        civilizationdata = []  # The civilization data for the executemany SQL function
        portdata = []  # The port data for the executemany SQL function
        totaljobs = 6

        # Get the star types from the database and store them in a list.
        starclass = []
        connection = db.stdb()
        query = "select `scid` from `starclass`"
        results = db.query(connection, query)
        for row in results:
            starclass.append(row["scid"])

        # Get the port types and store them in a list.
        portclass = []
        connection = db.stdb()
        query = "select * from `portclass`"
        presults = db.query(connection, query)
        for prow in presults:
            tempportclass = [prow['portclass'], prow['orecap'],
                             prow['organicscap'], prow['equipmentcap']]
            portclass.append(tempportclass)
        # Remove Class 0 ports from the list. They will be randomly placed during empire creation.
        portclass.pop(0)

        # * Create the Stardock in sector 0,0
        connection = db.stdb()
        query = "INSERT INTO `ports` (`portclass`, `portname`, `locationx`, `locationy`, `orecount`, `organicscount`, `equipmentcount`) VALUES (0, 'Stardock 001', 0, 0, 9000, 9000, 9000)"
        db.query(connection, query)
        portcounter = portcounter + 1

        # * BEGIN GALAXY CREATION
        # Create the sectors using a while loop.
        while sectorcount < totalsectors:  # Go through the number of sectors.
            # print("Sector Count: "+str(sectorcount))
            # While the height of the galaxy is less than the maximum height.
            while ydiametercount < diameter:
                # While the width of the galaxy is less than the maximum width.
                while xdiametercount < diameter:
                    # print("Coordinates: "+str(x)+","+str(y))

                    # Stars
                    rand = random.randrange(0, 100)
                    # The random numbers lands within the percentage.
                    if int(stars) <= rand:
                        # Randomly pick the number of stars in this sector.
                        systemstars = random.randrange(1, 8)
                        # Add to the total number of stars in the galaxy.
                        starcount = starcount + systemstars
                        # Set the loop counter.
                        starcounter = 0
                        while starcounter < systemstars:
                            # Randomly pick the class
                            scid = random.choice(starclass)
                            # Create the list of sector star details.
                            temp = (str(x), str(y), '', str(scid))
                            allstars.append(temp)
                            # Add to the total star tracker.
                            starcounter = starcounter + 1

                        # print("There is "+str(systemstars)+" star in this sector.")
                         # * Determine if there will be a port around this star.
                        portrand = random.randrange(0, 100)
                        if int(ports) <= portrand:
                            # Randomly pick the class
                            portclassval = random.randrange(0, len(portclass))
                            portname = "PORT-"+str(x)+"-"+str(y)
                            locationx = x
                            locationy = y
                            portore = random.randrange(
                                0, int(portclass[portclassval][1]))
                            portorganics = random.randrange(
                                0, int(portclass[portclassval][2]))
                            portequipment = random.randrange(
                                0, int(portclass[portclassval][3]))
                            temp = (portclassval, portname, locationx, locationy, portore,
                                    portorganics, portequipment)
                            if locationx != 0 and locationy != 0:
                                portdata.append(temp)
                            portcounter = portcounter + 1
                    else:  # There is no star.
                        # Calculate the odds of a rogue planet. Let's say 5%
                        rand = random.randrange(0, 100)
                        if roguechance <= rand:
                            # Create and save rogue planet.
                            planetcount = planetcount + 1
                            temp = (x, y, 8)
                            rogueplanets.append(temp)

                    # Coordinate cleanup
                    x = x+1
                    xdiametercount = xdiametercount+1
                    # Increase the sector count.
                    sectorcount = sectorcount + 1
                    # print("Sector count:"+str(sectorcount))
                    # print("Total Sectors:"+str(totalsectors))
                    # totalobjs = sectorcount+starcount+planetcount
                    # f = open("bigbangstats.txt", "w")
                    # f.write("Sector Number: "+str(sectorcount)+"\nStar Count: " +
                    #         str(starcount)+"\nPlanet Count: "+str(planetcount)+"\nSum: "+str(totalobjs))
                    # f.close()
                    if sectorcount == 1:
                        print("")
                        art.cd(
                            4, '', "Beginning galaxy creation. Depending on the number of sectors, this could take some time.", "reset", True)
                        text = "(1/"+str(totaljobs) + \
                            ") Dividing the galaxy into sectors..."
                        art.cd(
                            22, '', text, "reset", False)
                    elif sectorcount == int(totalsectors):
                        art.cd(15, '', "\t\t\t\t\t[ ", "reset", False)
                        art.cd(46, '', "DONE", "reset", False)
                        art.cd(15, '', " ]", "reset", True)

                x = radius*-1  # Bring this all the way back to the left.
                y = y-1  # Work your way down the y-axis
                xdiametercount = 0
                ydiametercount = ydiametercount+1

        # * ROGUE PLANETS
        # Display task text.
        text = "(2/"+str(totaljobs) + \
            ") Creating rogue planets..."
        art.cd(
            23, '', text, "reset", False)

        # Insert all the rogue planets.
        connection = db.stdb()
        query = "INSERT INTO `planets` (`x`, `y`, `pcid`) VALUES (%s,%s, %s)"
        db.querymany(connection, query, rogueplanets)

        # Task completed text.
        art.cd(15, '', "\t\t\t\t\t\t\t[ ", "reset", False)
        art.cd(46, '', "DONE", "reset", False)
        art.cd(15, '', " ]", "reset", True)

        # * STARS
        # Display task text.
        text = "(3/"+str(totaljobs) + \
            ") Forming stars..."
        art.cd(
            24, '', text, "reset", False)

        # Insert all the stars
        connection = db.stdb()
        # print(allstars)
        # print(rogueplanets)
        query = "INSERT INTO `stars` (`x`, `y`, `starname`, `scid`) VALUES (%s,%s, %s, %s)"
        db.querymany(connection, query, allstars)

        # Task completed text.
        art.cd(15, '', "\t\t\t\t\t\t\t\t[ ", "reset", False)
        art.cd(46, '', "DONE", "reset", False)
        art.cd(15, '', " ]", "reset", True)

        # * PLANETS
        # Display task text.
        text = "(4/"+str(totaljobs) + \
            ") Adding planets in orbit..."
        art.cd(
            25, '', text, "reset", False)
        # Get the planet types and store them in a list.
        planetclass = []
        connection = db.stdb()
        query = "select `pcid` from `planetclass`"
        results = db.query(connection, query)
        for row in results:
            planetclass.append(row["pcid"])
        # Drop the rogue planet pcid, as we do not need it in the list.
        planetclass.remove(8)

        # Query the stars for the sid
        connection = db.stdb()
        query = "select `sid`, `x`, `y` from `stars`"
        results = db.query(connection, query)
        for row in results:
            # Create the planets
            rand = random.randrange(0, 100)
            if int(planets) <= rand:
                # For each star, create a random number of planets up to 10.
                starplanets = random.randrange(1, 10)
                planetcount = planetcount + starplanets
                planetcounter = 0
                while planetcounter < starplanets:
                    pcid = random.choice(planetclass)
                    # * Determine if there will be a civilization on this planet.
                    rand = random.randrange(0, 100)
                    if rand <= civilizations:
                        civcounter = civcounter + 1
                        cid = civcounter
                        civname = "CIV"+str(cid)
                        temp = (row["x"], row["y"], civname)
                        civilizationdata.append(temp)
                    else:
                        cid = 0
                    temp = (row["x"], row["y"], row["sid"], pcid, cid)
                    planetswithstars.append(temp)
                    planetcounter = planetcounter + 1

        # Save the planets to the database.
        connection = db.stdb()
        query = "INSERT INTO `planets` (`x`, `y`, `sid`, `pcid`, `cid`) VALUES (%s, %s, %s, %s, %s)"
        db.querymany(connection, query, planetswithstars)

        # Task completed text.
        art.cd(15, '', "\t\t\t\t\t\t[ ", "reset", False)
        art.cd(46, '', "DONE", "reset", False)
        art.cd(15, '', " ]", "reset", True)

        # Display task text.
        text = "(5/"+str(totaljobs) + \
            ") Creating Life..."
        art.cd(
            26, '', text, "reset", False)

        # Save the civilizations to the database.
        connection = db.stdb()
        query = "INSERT INTO `civilizations` (`x`, `y`, `civname`) VALUES (%s, %s, %s)"
        db.querymany(connection, query, civilizationdata)

        # Task completed text.
        art.cd(15, '', "\t\t\t\t\t\t\t\t[ ", "reset", False)
        art.cd(46, '', "DONE", "reset", False)
        art.cd(15, '', " ]", "reset", True)

        # Display task text.
        text = "(6/"+str(totaljobs) + \
            ") Building Ports..."
        art.cd(
            27, '', text, "reset", False)
        # Save the ports to the database.
        connection = db.stdb()
        query = "INSERT INTO `ports` (`portclass`, `portname`, `locationx`, `locationy`, `orecount`, `organicscount`, `equipmentcount`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        db.querymany(connection, query, portdata)

        # Task completed text.
        art.cd(15, '', "\t\t\t\t\t\t\t\t[ ", "reset", False)
        art.cd(46, '', "DONE", "reset", False)
        art.cd(15, '', " ]", "reset", True)

        # * SUMMARY
        art.cd(226, '', str(sectorcount), "reset", False)
        art.cd(2, '', " sectors created.", "reset", True)
        art.cd(226, '', str(starcount), "reset", False)
        art.cd(2, '', " stars created.", "reset", True)
        art.cd(226, '', str(planetcount), "reset", False)
        art.cd(2, '', " planets created.", "reset", True)
        art.cd(226, '', str(civcounter), "reset", False)
        art.cd(2, '', " civilizations created.", "reset", True)
        art.cd(226, '', str(portcounter), "reset", False)
        art.cd(2, '', " ports built.", "reset", True)
        print("")
        art.cd(4, '', "Enjoy exploring the galaxy!", "reset", True)
        bbmenu(sectors, roguechance, stars, planets,
               civilizations, ports, empires)

    def bigdark():
        # Clear the Stars Table
        connection = db.stdb()
        query = "TRUNCATE `stars`"
        db.query(connection, query)
        # Clear the Planets Table
        connection = db.stdb()
        query = "TRUNCATE `planets`"
        db.query(connection, query)
        # Clear the Civilizations Table
        connection = db.stdb()
        query = "TRUNCATE `civilizations`"
        db.query(connection, query)
        # Clear the Ports Table
        connection = db.stdb()
        query = "TRUNCATE `ports`"
        db.query(connection, query)
        # Clear the Players Table
        connection = db.stdb()
        query = "TRUNCATE `players`"
        db.query(connection, query)
        # Clear the Logs Table
        connection = db.stdb()
        query = "TRUNCATE `logs`"
        db.query(connection, query)

        art.cd(23, '', "Once teeming with life, all the planets in the galaxy are no more. There shall never again be thought, love, or beauty experienced by anyone.", "reset", True)
        art.cd(22, '', "All the stars have been destroyed and the galaxy descends into darkness. Perhaps it is a blessing that there was no one around to see it.", "reset", True)
        print("")
        art.cd(4, '', "The galaxy has been destroyed. I really hope your galaxy isn't a simulation too.", "reset", True)
        print("")
        bbmenu(sectors, roguechance, stars, planets,
               civilizations, ports, empires)

    # Define default galaxy generation setting values
    sectors = 1000
    roguechance = 2
    stars = 50
    planets = 50
    civilizations = 10
    ports = 10
    empires = 3
    bbmenu(sectors, roguechance, stars, planets, civilizations, ports, empires)
    command = ""
    while command != "q":
        art.cd('light_cyan', '', "Design the galaxy ", 'reset', False)
        art.cd('226', '', "[?]", 'reset', False)
        art.cd('light_cyan', '', ": ", 'reset', False)
        command = input("")
        match command:
            case '1':
                sectors = ""
                while sectors.isdigit() == False:
                    print("")
                    sectors = input(
                        "How many sectors should exist in the galaxy? ")

                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case '2':
                roguechance = ""
                while roguechance.isdigit() == False:
                    print("")
                    roguechance = input(
                        "What chance is there of an empty sector having a rogue planet? ")

                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case '3':
                stars = ""
                while stars.isdigit() == False:
                    print("")
                    stars = input(
                        "What chance is there of a star forming in a sector? ")

                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case '4':
                planets = ""
                while planets.isdigit() == False:
                    print("")
                    planets = input(
                        "What chance is there that there will be planets around a star? ")

                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case '5':
                civilizations = ""
                while civilizations.isdigit() == False:
                    print("")
                    civilizations = input(
                        "What chance is there of a planet being inhabited? ")
                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case '6':
                ports = ""
                while ports.isdigit() == False:
                    print("")
                    ports = input(
                        "What chance is there of a port being in the sector? ")
                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case '7':
                empires = ""
                while empires.isdigit() == False:
                    print("")
                    empires = input("How many empires should be created? ")
                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case ('c' | 'C'):
                connection = db.stdb()
                query = "select * from `stars` LIMIT 1"
                results = db.rowcount(connection, query)
                if results != 0:
                    bigdark()
                else:
                    bigbang(sectors, roguechance, stars,
                            planets, civilizations, ports, empires)
                print("")
            case ('?' | ''):
                print("")
                bbmenu(sectors, roguechance, stars,
                       planets, civilizations, ports, empires)
            case ('q' | 'Q'):
                pass
            case _:
                art.cd(1, '', 'Command not found. Please try again.', "reset", True)
                print("")
