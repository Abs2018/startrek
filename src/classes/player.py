import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


class player():
    def __init__(self, pid):
        connection = db.stdb()
        query = "select * from `players` where `pid` = '"+str(pid)+"'"
        # print(query)
        results = db.query(connection, query)
        if results:
            for row in results:
                self.pid = row['pid']
                self.callsign = row['callsign']
                self.fname = row['fname']
                self.mname = row['mname']
                self.lname = row['lname']
                self.alignment = row['alignment']
                self.rank = row['rank']
                self.branch = row['branch']
                self.xp = row['xp']
                self.kills = row['kills']
                self.deaths = row['deaths']
                self.locationx = row['locationx']
                self.locationy = row['locationy']
                self.whereami = row['whereami']
                self.health = row['health']
                self.species = row['species']
                self.age = row['age']
                self.birthday = row['birthday']
                self.homeplanet = row['homeplanet']
                self.languages = row['languages']
        else:
            print("")
            art.cd(9, '', "Could not load the player information. Quitting.", 0, True)
            print("")
            quit()
