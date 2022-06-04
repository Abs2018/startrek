import mysql.connector
from mysql.connector import Error
from modules import db
from classes import shipClass
from modules import art
from classes import player
from classes import ship
shipClass = shipClass.shipClass()


def shipCreate(pid, shcid):
    # In here ask "What would you like to name your ship?"
    art.cd(
        'cyan', '', "What shall we name your brand new ship? ", 0, True)
    shipname = input("")
    # Get the shipclass values from the table
    # shipClass.shipClassAttributes(shcid)
    # Get the new owner info
    owner = player.player(pid)
    shipclassattr = ship.ship(shcid)

    # Save the ship
    connection = db.stdb()
    query = "INSERT INTO `ships` (`shipname`, `ownedby`, `ports`, `kills` , `shipclass`, `cloaked`, `locationx`, `locationy`, `fighters`, `shields`, `holds`, `invfuelore`, `invorganics`, `invequipment`, `invcolonists`, `genesistorpedoes`, `mines`, `markerbeacons`, `holoscanner`, `transwarpdrive`, `onplanetnum`, `cloakingdevices`, `interdicting`, `atomicdetonators`, `corbomitedevices`, `subspaceetherprobes`, `minedisruptors`, `photontorpedoes`, `psychicprobe`, `planetscanner`) VALUES ('" + \
        str(shipname)+"', '"+str(pid)+"', '0', '0', '"+str(shcid)+"', '0', '"+str(owner.locationx)+"', '"+str(owner.locationy)+"', '" + str(shipclassattr.fightersstart)+"', '"+str(shipclassattr.shieldsstart)+"', '"+str(shipclassattr.cargoholdsstart) + \
        "', '0', '0' ,'0', '0', '0', '0', '"+str(shipclassattr.markerbeaconsstart)+"', '0', '"+str(
            shipclassattr.transwarpdrive)+"', '0', '0', '0', '0', '0', '0', '0', '"+str(shipclassattr.photontorpedoesstart)+"', '0', '0')"
    db.query(connection, query)
    # print(query)


shipCreate(1, 2)
