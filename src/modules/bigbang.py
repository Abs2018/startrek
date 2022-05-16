# The Big Bang! This will create the game world.
import math
import random
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art

# TODO
# * Use a percentage to figure out if a planet will be inhabited.


def bb_main_menu():
    def bbmenu(sectors, stars, planets, civilizations, empires):
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
            art.cd(2, '', "How many sectors should exist in the galaxy? ", "", False)
            art.cd(226, '', str(sectors), "", True)

            # Row 2
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "2", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "What chance is there of a star forming in a sector? ", "", False)
            art.cd(226, '', str(stars), "", False)
            art.cd(226, '', "%", "", True)

            # Row 3
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "3", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(
                2, '', "What chance is there that there will be planets around a star? ", "", False)
            art.cd(226, '', str(planets), "", False)
            art.cd(226, '', "%", "", True)

            # Row 4
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "4", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(2, '', "How many civilizations should be created? ", "", False)
            art.cd(226, '', str(civilizations), "", True)

            # Row 5
            art.cd(5, '', "\t<", "", False)
            art.cd('light_cyan', '', "5", "", False)
            art.cd(5, '', "> ", "", False)
            art.cd(2, '', "How many empires should be created? ", "", False)
            art.cd(226, '', str(empires), "", True)

            # Row 6
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

    def bigbang(sectors, stars, planets, civilizations, empires):
        #!!!! Whatever changes you make in the bigbang function, please add the opposite in the bigdark function.
        # Get the star types from the database and store them in a list.
        starclass = []
        connection = db.stdb()
        query = "select `scid` from `starclass`"
        results = db.query(connection, query)
        for row in results:
            starclass.append(row["scid"])

        # Get the planet types and store them in a list.
        planetclass = []
        connection = db.stdb()
        query = "select `pcid` from `planetclass`"
        results = db.query(connection, query)
        for row in results:
            planetclass.append(row["pcid"])
        # Drop the rogue planet pcid, as we do not need it in the list.
        planetclass.remove(8)

        # Do the math around the sector coordinates. Our galaxies will be a square grid.

        # We add one to account for the 0,0 coordinates.
        diameter = int(math.sqrt(int(sectors)))+1
        # Total area of the galaxy equals length * width
        totalsectors = diameter * diameter
        #print("The galaxy will be "+str(diameter) +" sectors wide and tall for a total of "+str(totalsectors)+".")
        radius = math.floor(diameter/2)
        x = radius*-1
        y = radius
        # print(x)
        # print(y)
        sectorcount = 0
        xdiametercount = 0
        ydiametercount = 0
        starcount = 0  # Total number of stars created in the galaxy
        planetcount = 0  # Total number of planets created in the galaxy

        # Create the sectors using a while loop.
        while sectorcount < totalsectors:  # Go through the number of sectors.
            # print("Sector Count: "+str(sectorcount))
            # While the height of the galaxy is less than the maximum height.
            while ydiametercount < diameter:
                # While the width of the galaxy is less than the maximum width.
                while xdiametercount < diameter:
                    #print("Coordinates: "+str(x)+","+str(y))
                    # Stars
                    rand = random.randrange(0, 100)
                    # The random numbers lands within the percentage.
                    if int(stars) <= rand:
                        # Randomly pick the number of stars in this sector.
                        systemstars = random.randrange(1, 8)
                        starcount = starcount + systemstars
                        starcounter = 0
                        while starcounter < systemstars:
                            # Randomly pick the class
                            scid = random.choice(starclass)
                            # Insert into database. Get the sid of the star.
                            connection = db.stdb()
                            query = "INSERT INTO `stars` (`x`, `y`, `starname`, `scid`) VALUES ('"+str(
                                x)+"','"+str(y)+"','','"+str(scid)+"')"
                            cursor = connection.cursor(dictionary=True)
                            try:
                                cursor.execute(query)
                                # print("Query run successfully")
                                result = cursor.fetchall()
                            except Error as e:
                                # print(f"The error '{e}' occurred")
                                result = "FALSE"
                            connection.commit()
                            sid = cursor.lastrowid
                            connection.close()
                            starcounter = starcounter + 1
                            rand = random.randrange(0, 100)
                            if int(planets) <= rand:
                                # For each star, create a random number of planets up to 10.
                                starplanets = random.randrange(1, 10)
                                planetcount = planetcount + starplanets
                                planetcounter = 0
                                while planetcounter < starplanets:
                                    pcid = random.choice(planetclass)
                                    connection = db.stdb()
                                    query = "INSERT INTO `planets` (`x`, `y`, `sid`, `pcid`) VALUES ('"+str(
                                        x)+"','"+str(y)+"','"+str(sid)+"','"+str(pcid)+"')"
                                    db.query(connection, query)
                                    planetcounter = planetcounter + 1

                        #print("There is "+str(systemstars)+" star in this sector.")
                    else:  # There is no star.
                        # Calculate the odds of a rogue planet. Let's say 5%
                        rand = random.randrange(0, 100)
                        if 5 <= rand:
                            # Create and save rogue planet.
                            planetcount = planetcount + 1
                            connection = db.stdb()
                            query = "INSERT INTO `planets` (`x`, `y`, `pcid`) VALUES ('"+str(
                                x)+"','"+str(y)+"','8')"
                            db.query(connection, query)

                    # Coordinate cleanup
                    x = x+1
                    xdiametercount = xdiametercount+1
                    # Increase the sector count.
                    sectorcount = sectorcount + 1
                    #print("Sector count:"+str(sectorcount))
                    #print("Total Sectors:"+str(totalsectors))
                    if sectorcount == 1:
                        print("")
                        art.cd(
                            4, '', "Beginning galaxy creation. Depending on the number of sectors, this could take some time.", "reset", True)
                    elif sectorcount == int(totalsectors*0.1):
                        art.cd(22, '', "10% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.2):
                        art.cd(23, '', "20% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.3):
                        art.cd(24, '', "30% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.4):
                        art.cd(25, '', "40% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.5):
                        art.cd(26, '', "50% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.6):
                        art.cd(27, '', "60% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.7):
                        art.cd(28, '', "70% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.8):
                        art.cd(29, '', "80% completed...", "reset", True)
                    elif sectorcount == int(totalsectors*0.9):
                        art.cd(30, '', "90% completed...", "reset", True)
                    elif sectorcount == int(totalsectors):
                        art.cd(31, '', "100% completed...", "reset", True)

                x = radius*-1  # Bring this all the way back to the left.
                y = y-1  # Work your way down the y-axis
                xdiametercount = 0
                ydiametercount = ydiametercount+1

        art.cd(226, '', str(sectorcount), "reset", False)
        art.cd(2, '', " sectors created.", "reset", True)
        art.cd(226, '', str(starcount), "reset", False)
        art.cd(2, '', " stars created.", "reset", True)
        art.cd(226, '', str(planetcount), "reset", False)
        art.cd(2, '', " planets created.", "reset", True)
        print("")
        art.cd(4, '', "Enjoy exploring the galaxy!", "reset", True)

    def bigdark():
        # Clear the Stars Table
        connection = db.stdb()
        query = "TRUNCATE `stars`"
        db.query(connection, query)
        # Clear the Planets Table
        connection = db.stdb()
        query = "TRUNCATE `planets`"
        db.query(connection, query)
        daletegalaxy = False
        art.cd(23, '', "Once teeming with life, all the planets in the galaxy are no more. There shall never again be thought, love, or beauty experienced by anyone.", "reset", True)
        art.cd(22, '', "All the stars have been destroyed and the galaxy descends into darkness. Perhaps it is a blessing that there was no one around to see it.", "reset", True)
        print("")
        art.cd(4, '', "The galaxy has been destroyed. I really hope our galaxy isn't a simulation too.", "reset", True)
        print("")
        bbmenu(sectors, stars, planets, civilizations, empires)

    # Define default galaxy generation setting values
    sectors = 100
    stars = 50
    planets = 50
    civilizations = 10
    empires = 3
    bbmenu(sectors, stars, planets, civilizations, empires)
    command = ""
    while command != "q":
        art.cd('light_cyan', '', "Design the galaxy ", 'reset', False)
        art.cd('226', '', "[?]", 'reset', False)
        art.cd('light_cyan', '', ": ", 'reset', False)
        command = input("")
        match command:
            case '1':
                sectors = input("How many sectors exist in the galaxy? ")
                print("")
                bbmenu(sectors, stars, planets, civilizations, empires)
            case '2':
                stars = input(
                    "What chance is there of a star forming in a sector? ")
                print("")
                bbmenu(sectors, stars, planets, civilizations, empires)
            case '3':
                planets = input(
                    "What chance is there that there will be planets around a star? ")
                print("")
                bbmenu(sectors, stars, planets, civilizations, empires)
            case '4':
                civilizations = input(
                    "How many civilizations should be created? ")
                print("")
                bbmenu(sectors, stars, planets, civilizations, empires)
            case '5':
                empires = input("How many empires should be created? ")
                print("")
                bbmenu(sectors, stars, planets, civilizations, empires)
            case ('c' | 'C'):
                connection = db.stdb()
                query = "select * from `stars` LIMIT 1"
                results = db.rowcount(connection, query)
                if results != 0:
                    bigdark()
                else:
                    bigbang(sectors, stars, planets, civilizations, empires)
                print("")
            case ('?' | ''):
                print("")
                bbmenu(sectors, stars, planets, civilizations, empires)
            case ('q' | 'Q'):
                pass
            case _:
                art.cd(1, '', 'Command not found. Please try again.', "reset", True)
                print("")
