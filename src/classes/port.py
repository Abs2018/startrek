import mysql.connector
from mysql.connector import Error
from modules import db


class port():
    def __init__(self, x, y):
        connection = db.stdb()
        query = "select * from `ports` where `locationx` = '" + \
            str(x)+"' and `locationy` = '"+str(y)+"'"
        # print(query)
        results = db.query(connection, query)
        for row in results:
            self.portclass = row['portclass']
            self.portname = row['portname']
            self.locationx = row['locationx']
            self.locationy = row['locationy']
            self.orecount = row['orecount']
            self.organicscount = row['organicscount']
            self.equipmentcount = row['equipmentcount']
