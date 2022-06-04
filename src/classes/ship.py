import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


class ship():
    def __init__(self, pid):
        connection = db.stdb()
        query = "SELECT * FROM `ships` WHERE `ownedby` = '" + \
            str(pid)+"' AND `active`='1'"
        # print(query)
        results = db.query(connection, query)
        if results:
            for row in results:
                self.ship = row['shid']
                self.shipname = row['shipname']
                self.ownedby = row['ownedby']
                self.ports = row['ports']
                self.kills = row['kills']
                self.shipclass = row['shipclass']
                self.cloaked = row['cloaked']
                self.locationx = row['locationx']
                self.locationy = row['locationy']
                self.fighters = row['fighters']
                self.shields = row['shields']
                self.holds = row['holds']
                self.invfuelore = row['invfuelore']
                self.invorganics = row['invorganics']
                self.invequipment = row['invequipment']
                self.invcolonists = row['invcolonists']
                self.genesistorpedoes = row['genesistorpedoes']
                self.mines = row['mines']
                self.markerbeacons = row['markerbeacons']
                self.holoscanner = row['holoscanner']
                self.transwarpdrive = row['transwarpdrive']
                self.onplanetnum = row['onplanetnum']
                self.cloakingdevices = row['cloakingdevices']
                self.interdicting = row['interdicting']
                self.atomicdetonators = row['atomicdetonators']
                self.corbomitedevices = row['corbomitedevices']
                self.subspaceetherprobes = row['subspaceetherprobes']
                self.minedisruptors = row['minedisruptors']
                self.photontorpedoes = row['photontorpedoes']
                self.psychicprobe = row['psychicprobe']
                self.planetscanner = row['planetscanner']
        else:
            print("")
            art.cd(9, '', "Could not load the ship information. Quitting.", 0, True)
            print("")
            quit()
