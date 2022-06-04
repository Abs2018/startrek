import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


class shipClassInfo():
    def __init__(self, shcid):
        connection = db.stdb()
        query = "SELECT * FROM `shipclass` WHERE `shcid` = '"+str(shcid)+"'"
        results = db.query(connection, query)
        if results:
            for row in results:
                self.shcid = row['shcid']
                self.shipclassname = row['shipclassname']
                self.fgcolour = row['fgcolour']
                self.bgcolour = row['bgcolour']
                self.alignment = row['alignment']
                self.manufacturer = row['manufacturer']
                self.cargoholdsstart = row['cargoholdsstart']
                self.cargoholdsmax = row['cargoholdsmax']
                self.fightersstart = row['fightersstart']
                self.fightersmax = row['fightersmax']
                self.fighterattackforce = row['fighterattackforce']
                self.photontorpedoesstart = row['photontorpedoesstart']
                self.photontorpedoesmax = row['photontorpedoesmax']
                self.shieldsstart = row['shieldsstart']
                self.shieldsmax = row['shieldsmax']
                self.minesstart = row['minesstart']
                self.minesmax = row['minesmax']
                self.minedisruptorsstart = row['minedisruptorsstart']
                self.minedisruptorsmax = row['minedisruptorsmax']
                self.markerbeaconsstart = row['markerbeaconsstart']
                self.markerbeaconsmax = row['markerbeaconsmax']
                self.genesistorpedoes = row['genesistorpedoes']
                self.cloakingdevices = row['cloakingdevices']
                self.atomicdetonators = row['atomicdetonators']
                self.corbomitedevices = row['corbomitedevices']
                self.subspaceetherprobes = row['subspaceetherprobes']
                self.transporterrange = row['transporterrange']
                self.offensiveodds = row['offensiveodds']
                self.defensiveodds = row['defensiveodds']
                self.scannerdensity = row['scannerdensity']
                self.scannerholo = row['scannerholo']
                self.transwarpdrive = row['transwarpdrive']
                self.fusiondrive = row['fusiondrive']
                self.planetscanner = row['planetscanner']
                self.interdictorgenerator = row['interdictorgenerator']
                self.usedasescapepod = row['usedasescapepod']
                self.carriesescapepod = row['carriesescapepod']
                self.escapepodclass = row['escapepodclass']
                self.canlandonplanet = row['canlandonplanet']
                self.defensiveguardianbonus = row['defensiveguardianbonus']
                self.requirefedcommission = row['requirefedcommission']
                self.requiredxp = row['requiredxp']
                self.requirecorporatestatus = row['requirecorporatestatus']
                self.requireceostatus = row['requireceostatus']
                self.costofholdspace = row['costofholdspace']
                self.costofdrive = row['costofdrive']
                self.costofcomputersystem = row['costofcomputersystem']
                self.costofshipshull = row['costofshipshull']
            # shipattributes = {"shcid": shcid, "shipclassname": shipclassname, "fgcolour": fgcolour, "bgcolour": bgcolour, "alignment": alignment, "manufacturer": manufacturer, "cargoholdsstart": cargoholdsstart, "cargoholdsmax": cargoholdsmax, "fightersstart": fightersstart, "fightersmax": fightersmax, "fighterattackforce": fighterattackforce, "photontorpedoesstart": photontorpedoesstart, "photontorpedoesmax": photontorpedoesmax,  "shieldsstart": shieldsstart, "shieldsmax": shieldsmax, "minesstart": minesstart, "minesmax": minesmax, "minedisruptorsstart": minedisruptorsstart, "minedisruptorsmax": minedisruptorsmax, "markerbeaconsstart": markerbeaconsstart, "markerbeaconsmax": markerbeaconsmax, "genesistorpedoes": genesistorpedoes, "cloakingdevices": cloakingdevices, "atomicdetonators": atomicdetonators, "corbomitedevices": corbomitedevices, "subspaceetherprobes": subspaceetherprobes, "transporterrange": transporterrange, "offensiveodds": offensiveodds, "defensiveodds": defensiveodds, "scannerdensity": scannerdensity, "scannerholo": scannerholo, "transwarpdrive": transwarpdrive, "fusiondrive": fusiondrive, "planetscanner": planetscanner, "interdictorgenerator": interdictorgenerator, "usedasescapepod": usedasescapepod, "carriesescapepod": carriesescapepod, "escapepodclass": escapepodclass, "canlandonplanet": canlandonplanet, "defensiveguardianbonus": defensiveguardianbonus, "requirefedcommission": requirefedcommission, "requiredxp": requiredxp, "requirecorporatestatus": requirecorporatestatus, "requireceostatus": requireceostatus, "costofholdspace": costofholdspace, "costofdrive": costofdrive, "costofcomputersystem": costofcomputersystem, "costofshipshull": costofshipshull}
            # return shipattributes
        else:
            print("")
            art.cd(9, '', "Could not load the ship class. Quitting.", 0, True)
            print("")
            quit()
