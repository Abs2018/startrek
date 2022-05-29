import mysql.connector
from mysql.connector import Error
from modules import db


class player():
    def __init__(self, pid):
        connection = db.stdb()
        query = "select * from `players` where `pid` = '"+str(pid)+"'"
        results = db.query(connection, query)
        for row in results:
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
