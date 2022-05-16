# https://tutorialedge.net/python/python-multiprocessing-tutorial/

import multiprocessing as mp

sectors = 1000
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


def bigbanggen(x, y):
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
            #connection = db.stdb()
            print = "INSERT INTO `stars` (`x`, `y`, `starname`, `scid`) VALUES ('"+str(
                    x)+"','"+str(y)+"','','"+str(scid)+"')"
            #cursor = connection.cursor(dictionary=True)
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


# Create the sectors using a while loop.
while sectorcount < totalsectors:  # Go through the number of sectors.
    # print("Sector Count: "+str(sectorcount))
    # While the height of the galaxy is less than the maximum height.
    while ydiametercount < diameter:
        # While the width of the galaxy is less than the maximum width.
        while xdiametercount < diameter:
            #print("Coordinates: "+str(x)+","+str(y))
            bigbanggen(x, y)
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
