from classes import log
from dataclasses import dataclass
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
from classes import playerClass
playerClass = playerClass.player()
log = log.log()
# TODO:
# *


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
            # Get the last time and date that someone docked here, and assign XP as desired.

            # Update port last docked time.

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
