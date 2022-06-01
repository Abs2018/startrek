from dataclasses import dataclass
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
from classes import log
log = log.log()
# TODO:
# *


@dataclass
class stationClass():
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
