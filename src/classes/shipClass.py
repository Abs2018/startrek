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
class shipClass():
    def __init__(self):
        pass

    '''
    This function returns all the attributes of the specific ship class.
    '''

    def shipAttributes(self, shcid):
        connection = db.stdb()
        query = "select * from `shipclass` where `shcid` = '"+str(shcid)+"'"
        # print(query)
        results = db.query(connection, query)
        if results:
            for row in results:
                shcid = row['shcid']
                shipclassname = row['shipclassname']
                fgcolour = row['fgcolour']
                bgcolour = row['bgcolour']
                alignment = row['alignment']
                manufacturer = row['manufacturer']
                cargoholdsstart = row['cargoholdsstart']
                cargoholdsmax = row['cargoholdsmax']
                fightersstart = row['fightersstart']
                fightersmax = row['fightersmax']
                fighterattackforce = row['fighterattackforce']
                photontorpedoesstart = row['photontorpedoesstart']
                photontorpedoesmax = row['photontorpedoesmax']
                shieldsstart = row['shieldsstart']
                shieldsmax = row['shieldsmax']
                minesstart = row['minesstart']
                minesmax = row['minesmax']
                minedisruptorsstart = row['minedisruptorsstart']
                minedisruptorsmax = row['minedisruptorsmax']
                markerbeaconsstart = row['markerbeaconsstart']
                markerbeaconsmax = row['markerbeaconsmax']
                genesistorpedoes = row['genesistorpedoes']
                cloakingdevices = row['cloakingdevices']
                atomicdetonators = row['atomicdetonators']
                corbomitedevices = row['corbomitedevices']
                subspaceetherprobes = row['subspaceetherprobes']
                transporterrange = row['transporterrange']
                offensiveodds = row['offensiveodds']
                defensiveodds = row['defensiveodds']
                scannerdensity = row['scannerdensity']
                scannerholo = row['scannerholo']
                transwarpdrive = row['transwarpdrive']
                fusiondrive = row['fusiondrive']
                planetscanner = row['planetscanner']
                interdictorgenerator = row['interdictorgenerator']
                usedasescapepod = row['usedasescapepod']
                carriesescapepod = row['carriesescapepod']
                escapepodclass = row['escapepodclass']
                canlandonplanet = row['canlandonplanet']
                defensiveguardianbonus = row['defensiveguardianbonus']
                requirefedcommission = row['requirefedcommission']
                requiredxp = row['requiredxp']
                requirecorporatestatus = row['requirecorporatestatus']
                requireceostatus = row['requireceostatus']
                costofholdspace = row['costofholdspace']
                costofdrive = row['costofdrive']
                costofcomputersystem = row['costofcomputersystem']
                costofshipshull = row['costofshipshull']
            shipattributes = {"shcid": shcid, "shipclassname": shipclassname, "fgcolour": fgcolour, "bgcolour": bgcolour, "alignment": alignment, "manufacturer": manufacturer, "cargoholdsstart": cargoholdsstart, "cargoholdsmax": cargoholdsmax, "fightersstart": fightersstart, "fightersmax": fightersmax, "fighterattackforce": fighterattackforce, "photontorpedoesstart": photontorpedoesstart, "photontorpedoesmax": photontorpedoesmax,  "shieldsstart": shieldsstart, "shieldsmax": shieldsmax, "minesstart": minesstart, "minesmax": minesmax, "minedisruptorsstart": minedisruptorsstart, "minedisruptorsmax": minedisruptorsmax, "markerbeaconsstart": markerbeaconsstart, "markerbeaconsmax": markerbeaconsmax, "genesistorpedoes": genesistorpedoes, "cloakingdevices": cloakingdevices, "atomicdetonators": atomicdetonators, "corbomitedevices": corbomitedevices,
                              "subspaceetherprobes": subspaceetherprobes, "transporterrange": transporterrange, "offensiveodds": offensiveodds, "defensiveodds": defensiveodds, "scannerdensity": scannerdensity, "scannerholo": scannerholo, "transwarpdrive": transwarpdrive, "fusiondrive": fusiondrive, "planetscanner": planetscanner, "interdictorgenerator": interdictorgenerator, "usedasescapepod": usedasescapepod, "carriesescapepod": carriesescapepod, "escapepodclass": escapepodclass, "canlandonplanet": canlandonplanet, "defensiveguardianbonus": defensiveguardianbonus, "requirefedcommission": requirefedcommission, "requiredxp": requiredxp, "requirecorporatestatus": requirecorporatestatus, "requireceostatus": requireceostatus, "costofholdspace": costofholdspace, "costofdrive": costofdrive, "costofcomputersystem": costofcomputersystem, "costofshipshull": costofshipshull}
            return shipattributes
        else:
            print("")
            art.cd(9, '', "Could not load the ship class. Quitting.")
            print("")
            quit()

    '''
    This function creates a ship class using the ship editor in the admin console.
    '''

    def shipClassCreate(self):
        totalquestions = 47

        print("")
        art.cd(226, '', "\t\t\tCREATE A NEW SHIP", "", True)
        print("")
        # art.cd('light_cyan', '', "C", "", False)
        # art.cd(5, '', "> ", "", False)
        art.cd(2, '', "Let's create a new ship. We will ask you ", "", False)
        art.cd('light_cyan', '', str(totalquestions), "", False)
        art.cd(2, '', " total questions, so this will be a marathon, not a sprint. When we are done, though, you will have a brand new ship class to explore the galaxy with! ", "", True)
        i = 1
        # shipclassname
        shipclassname = ""
        while shipclassname == "":
            print("")
            art.cd(123, '', "CLASS NAME", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(2, '', "What class of ship is this? (eg: Constitution): ", "", False)
            shipclassname = input()
        i = i + 1

        # fgcolour
        fgcolour = ""
        while fgcolour == "":
            print("")
            art.cd(123, '', "COLOURS", "", True)

            art.cd(
                3, '', "\tBlack\tRed\tGreen\tYellow\tBlue\tPurple\tCyan\tWhite", "", True)
            art.cd(3, '', "Dim\t", "", False)
            art.cd(0, '', "0\t", '', False)
            art.cd(1, '', "1\t", '', False)
            art.cd(2, '', "2\t", '', False)
            art.cd(3, '', "3\t", '', False)
            art.cd(4, '', "4\t", '', False)
            art.cd(5, '', "5\t", '', False)
            art.cd(6, '', "6\t", '', False)
            art.cd(7, '', "7\t", 0, True)
            art.cd(3, '', "Normal\t", "", False)
            art.cd(8, '', "8\t", '', False)
            art.cd(9, '', "9\t", '', False)
            art.cd(10, '', "10\t", '', False)
            art.cd(11, '', "11\t", '', False)
            art.cd(12, '', "12\t", '', False)
            art.cd(13, '', "13\t", '', False)
            art.cd(14, '', "14\t", '', False)
            art.cd(15, '', "15\t", 0, True)
            art.cd(3, '', "Bright\t", "", False)
            art.cd(232, '', "232\t", '', False)
            art.cd(196, '', "196\t", '', False)
            art.cd(82, '', "82\t", '', False)
            art.cd(226, '', "226\t", '', False)
            art.cd(27, '', "27\t", '', False)
            art.cd(207, '', "207\t", '', False)
            art.cd(123, '', "123\t", '', False)
            art.cd(255, '', "255\t", 0, True)

            print("")
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "What colour font should the text be in the game?: ", "", False)
            fgcolour = input()
        i = i + 1

        # bgcolour
        bgcolour = ""
        while bgcolour == "":
            print("")
            art.cd(123, '', "BACKGROUND COLOURS", "", True)

            art.cd(
                3, '', "\tBlack\tRed\tGreen\tYellow\tBlue\tPurple\tCyan\tWhite", "", True)
            art.cd(3, '', "Dim\t", "", False)
            art.cd(255, 0, "0  \t", '', False)
            art.cd(255, 1, "1  \t", '', False)
            art.cd(255, 2, "2  \t", '', False)
            art.cd(255, 3, "3  \t", '', False)
            art.cd(255, 4, "4  \t", '', False)
            art.cd(255, 5, "5  \t", '', False)
            art.cd(255, 6, "6  \t", '', False)
            art.cd(0, 7, "7  \t", 0, True)
            art.cd(3, '', "Normal\t", "", False)
            art.cd(255, 8, "8  \t", '', False)
            art.cd(255, 9, "9  \t", '', False)
            art.cd(0, 10, "10 \t", '', False)
            art.cd(0, 11, "11 \t", '', False)
            art.cd(255, 12, "12 \t", '', False)
            art.cd(255, 13, "13 \t", '', False)
            art.cd(0, 14, "14 \t", '', False)
            art.cd(0, 15, "15 \t", 0, True)
            art.cd(3, '', "Bright\t", "", False)
            art.cd(255, 232, "232\t", '', False)
            art.cd(255, 196, "196\t", '', False)
            art.cd(0, 82, "82 \t", '', False)
            art.cd(0, 226, "226\t", '', False)
            art.cd(255, 27, "27 \t", '', False)
            art.cd(255, 207, "207\t", '', False)
            art.cd(0, 123, "123\t", '', False)
            art.cd(0, 255, "255\t", 0, True)

            print("")
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "What should the background colour of the text be? Type '999' for no background: ", "", False)
            bgcolour = input()
        i = i + 1

        # alignment
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1

        # manufacturer
        print("")
        art.cd(123, '', "MANUFACTURER", "", True)
        art.cd(5, '', "(", "", False)
        art.cd('light_cyan', '', str(i)+"/" +
               str(totalquestions), "", False)
        art.cd(5, '', ") ", "", False)
        art.cd(2, '', "Who is the manufacturer of this ship? If blank, one will randomly be chosen: ", "", False)
        manufacturer = input()

        #! Check to see if manufacturer is empty. If so, choose random manufacturer that aligns with empire or 'none'.

        i = i + 1

        # cargoholdsstart
        cargoholdsstart = ""
        while cargoholdsstart == "":
            print("")
            art.cd(123, '', "STARTING CARGO HOLDS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many cargo holds does this ship start with?: ", "", False)
            cargoholdsstart = input()
        i = i + 1

        # cargoholdsmax
        cargoholdsmax = ""
        while cargoholdsmax == "":
            print("")
            art.cd(123, '', "MAXIMUM CARGO HOLDS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many cargo holds can this ship have in total?: ", "", False)
            cargoholdsmax = input()
        i = i + 1

        # fightersstart
        fightersstart = ""
        while fightersstart == "":
            print("")
            art.cd(123, '', "STARTING FIGHTER COMPLIMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many fighters does this ship start with?: ", "", False)
            fightersstart = input()
        i = i + 1

        # fightersmax
        fightersmax = ""
        while fightersmax == "":
            print("")
            art.cd(123, '', "MAXIMUM FIGHTERS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many total fighters can this ship carry?: ", "", False)
            fightersmax = input()
        i = i + 1

        # fighterattackforce
        fighterattackforce = ""
        while fighterattackforce == "":
            print("")
            art.cd(123, '', "FIGHTER ATTACK FORCE", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many fighters can this ship launch in one attack?: ", "", False)
            fighterattackforce = input()
        i = i + 1

        # photontorpedoesstart
        photontorpedoesstart = ""
        while photontorpedoesstart == "":
            print("")
            art.cd(123, '', "STARTING PHOTON TORPEDO COMPLIMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many photon torpedoes does this ship start with?: ", "", False)
            photontorpedoesstart = input()
        i = i + 1

        # photontorpedoesmax
        photontorpedoesmax = ""
        while photontorpedoesmax == "":
            print("")
            art.cd(123, '', "MAXIMUM PHOTON TORPEDO COMPLIMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many photon torpedoes can this ship carry?: ", "", False)
            photontorpedoesmax = input()
        i = i + 1

        # shieldsstart
        shieldsstart = ""
        while shieldsstart == "":
            print("")
            art.cd(123, '', "INITIAL SHIELD LEVEL", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many shields does this ship come with?: ", "", False)
            shieldsstart = input()
        i = i + 1

        # shieldsmax
        shieldsmax = ""
        while shieldsmax == "":
            print("")
            art.cd(123, '', "MAXIMUM SHIELD LEVEL", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many shields can this ship sustain?: ", "", False)
            shieldsmax = input()
        i = i + 1

        # minesstart
        minesstart = ""
        while minesstart == "":
            print("")
            art.cd(123, '', "STARTING MINE COUNT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many mines does this ship come with?: ", "", False)
            minesstart = input()
        i = i + 1

        # minesmax
        minesmax = ""
        while minesmax == "":
            print("")
            art.cd(123, '', "MAXIMUM MINE COUNT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "What is the total amount of mines this ship can carry?: ", "", False)
            minesmax = input()
        i = i + 1

        # minedisruptorsstart
        minedisruptorsstart = ""
        while minedisruptorsstart == "":
            print("")
            art.cd(123, '', "INITIAL MINE DISRUPTORS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many mine disruptors does this ship start with?: ", "", False)
            minedisruptorsstart = input()
        i = i + 1

        # minedisruptorsmax
        minedisruptorsmax = ""
        while minedisruptorsmax == "":
            print("")
            art.cd(123, '', "MAXIMUM MINE DISTRUPTORS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Maximum number of mine disruptors the ship can carry: ", "", False)
            minedisruptorsmax = input()
        i = i + 1

        # markerbeaconsstart
        markerbeaconsstart = ""
        while markerbeaconsstart == "":
            print("")
            art.cd(123, '', "INITIAL MARKER BEACON COUNT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many marker beacons should this ship start with?: ", "", False)
            markerbeaconsstart = input()
        i = i + 1

        # markerbeaconsmax
        markerbeaconsmax = ""
        while markerbeaconsmax == "":
            print("")
            art.cd(123, '', "MAXIMUM MARKER BEACON COUNT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many marker beacons can this ship carry?: ", "", False)
            markerbeaconsmax = input()
        i = i + 1

        # genesistorpedoes
        genesistorpedoes = ""
        while genesistorpedoes == "":
            print("")
            art.cd(123, '', "MAXIMUM GENESIS TORPEDOES", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "All ships start with 0 Genesis Torpedoes. What is the maximum amount of Genesis Torpedoes this ship can hold?: ", "", False)
            genesistorpedoes = input()
        i = i + 1

        # cloakingdevices
        cloakingdevices = ""
        while cloakingdevices == "":
            print("")
            art.cd(123, '', "MAXIMUM CLOAKING DEVICES", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many single-use cloaking devices can this ship carry?: ", "", False)
            cloakingdevices = input()
        i = i + 1

        # atomicdetonators
        atomicdetonators = ""
        while atomicdetonators == "":
            print("")
            art.cd(123, '', "AROMIC DETONATORS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many planet destroying atomic detonators can this ship carry?: ", "", False)
            atomicdetonators = input()
        i = i + 1

        # corbomitedevices
        corbomitedevices = ""
        while corbomitedevices == "":
            print("")
            art.cd(123, '', "CORBOMITE DEVICES", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How mant corbomite devices can this ship be packed with?: ", "", False)
            corbomitedevices = input()
        i = i + 1

        # subspaceetherprobes
        subspaceetherprobes = ""
        while subspaceetherprobes == "":
            print("")
            art.cd(123, '', "SUBSPACE ETHERPROBES", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "How many subspace etherprobes can this ship have?: ", "", False)
            subspaceetherprobes = input()
        i = i + 1

        # transporterrange
        transporterrange = ""
        while transporterrange == "":
            print("")
            art.cd(123, '', "TRANSPORTER RANGE", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "What is this ship's transporter range?: ", "", False)
            transporterrange = input()
        i = i + 1

        # offensiveodds
        offensiveodds = ""
        while offensiveodds == "":
            print("")
            art.cd(123, '', "OFFENSIVE ODDS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Compared to a basic ship, how much more offensive capability does this ship have? (eg: 1.2): ", "", False)
            offensiveodds = input()
        i = i + 1

        # defensiveodds
        defensiveodds = ""
        while defensiveodds == "":
            print("")
            art.cd(123, '', "DEFENSIVE ODDS", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Compared to a basic ship, how much more defensive capability does this ship have? (eg: 1.2): ", "", False)
            defensiveodds = input()
        i = i + 1

        # scannerdensity
        scannerdensity = ""
        while scannerdensity == "":
            print("")
            art.cd(123, '', "DENSITY SCANNER", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Can this ship have a density scanner?: ", "", False)
            scannerdensity = input()
        i = i + 1

        # scannerholo
        scannerholo = ""
        while scannerholo == "":
            print("")
            art.cd(123, '', "HOLO SCANNER", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            scannerholo = input()
        i = i + 1

        # transwarpdrive
        transwarpdrive = ""
        while transwarpdrive == "":
            print("")
            art.cd(123, '', "TRANSWARP DRIVE", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Can this ship have a transwarp drive?: ", "", False)
            transwarpdrive = input()
        i = i + 1

        # fusiondrive
        fusiondrive = ""
        while fusiondrive == "":
            print("")
            art.cd(123, '', "FUSION DRIVE", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Can this ship have a fusion drive?: ", "", False)
            fusiondrive = input()
        i = i + 1

        # planetscanner
        planetscanner = ""
        while planetscanner == "":
            print("")
            art.cd(123, '', "PLANET SCANNER", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Can this ship have a planet scanner?: ", "", False)
            planetscanner = input()
        i = i + 1

        # interdictorgenerator = row['interdictorgenerator']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # usedasescapepod = row['usedasescapepod']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # carriesescapepod = row['carriesescapepod']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # escapepodclass = row['escapepodclass']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # canlandonplanet = row['canlandonplanet']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # defensiveguardianbonus = row['defensiveguardianbonus']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # requirefedcommission = row['requirefedcommission']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # requiredxp = row['requiredxp']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # requirecorporatestatus = row['requirecorporatestatus']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # requireceostatus = row['requireceostatus']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # costofholdspace = row['costofholdspace']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # costofdrive = row['costofdrive']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # costofcomputersystem = row['costofcomputersystem']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1
        # costofshipshull = row['costofshipshull']
        alignment = ""
        while alignment == "":
            print("")
            art.cd(123, '', "ALIGNMENT", "", True)
            art.cd(5, '', "(", "", False)
            art.cd('light_cyan', '', str(i)+"/" +
                   str(totalquestions), "", False)
            art.cd(5, '', ") ", "", False)
            art.cd(
                2, '', "Which empire can this ship class be purchased in? '1' for any empire: ", "", False)
            alignment = input()
        i = i + 1

        # Save the ship into the table.

    def shipClassesView(self):
        connection = db.stdb()
        query = "select `shcid`,`shipclassname`,`fgcolour`,`bgcolour` from `shipclass`"
        # print(query)
        results = db.query(connection, query)
        if results:
            print("")
            art.cd(226, '', "\t\t\tSHIP CLASSES", "", True)
            print("")
            for row in results:
                art.cd(13, '', " <", '', False)
                art.cd(2, '', str(row['shcid']), '', False)
                art.cd(13, '', "> ", '', False)
                if str(row['bgcolour']) == '999':
                    row['bgcolour'] = ''
                art.cd(str(row['fgcolour']), str(row['bgcolour']),
                       str(row['shipclassname']), 0, True)
            print("")
