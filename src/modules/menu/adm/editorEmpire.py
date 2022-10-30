# Import the required modules.
from modules import db
from modules import art
from modules.menu.adm import main
from modules import func

def displayEmpires():
    func.clear()
    # Display all Empires
    connection = db.stdb()
    query = "select * from `empires`"
    results = db.query(connection, query)

    print("")
    art.cd(226, '', "\t\t\tDISPLAYING ALL EMPIRES", "", True)
    print("")
    for row in results:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', str(row['eid']), "", False)
        art.cd(5, '', "> ", "", False)
        art.cd(2, '', row['empname'], "", True)
    command = ""

def changeEmpireName(eid):
    func.clear()
    while True:
        print("")
        art.cd('light_cyan', '', "New Empire Name:", 0, False)
        empireName = input(" ")
        if empireName:
            break
    connection = db.stdb()
    query = "UPDATE `empires` SET `empname`='" + \
        empireName+"' WHERE `eid`='"+str(eid)+"'"
    # print(query)
    db.query(connection, query)
    return empireName

def changeSpaceForceName(eid):
    func.clear()
    while True:
        print("")
        art.cd('light_cyan', '', "New Space Force Name:", 0, False)
        SpaceForceName = input(" ")
        if SpaceForceName:
            break
    connection = db.stdb()
    query = "UPDATE `empires` SET `spaceforce`='" + \
        SpaceForceName+"' WHERE `eid`='"+str(eid)+"'"
    # print(query)
    db.query(connection, query)
    return SpaceForceName

def changeSecID(eid):
    func.clear()
    pass

def changeX(eid):
    func.clear()
    pass

def changeY(eid):
    func.clear()
    pass

def deleteEmpire(eid):
    func.clear()
    # 2022-10-30: There is a lot more to this than deleting the empire name. You have to delete all the ships, planet alignments, etc. Save this for last because you don't know what an empire looks like yet.
    pass


def menu():
    command = ""
    while command != "q":
        if command == "":
            print("")
            art.cd(5, '', "[Empire Editor] ", '', False)
            art.cd('light_cyan', '',
                   "Which empire would you like to edit? ", 0, False)
            art.cd(226, '', "[?]", '', False)
            art.cd('light_cyan', '', ": ", 0, False)
            command = input(" ")

        match command:
            case ('?' | ''):
                displayEmpires()
                menu()
            case ('q' | 'Q'):
                main.menu()
            case _:
                # Get the user's information
                connection = db.stdb()
                query = "select * from `empires` where `eid`='"+command+"'"
                results = db.query(connection, query)
                if results:
                    for row in results:
                        eid = row['eid']
                        empirename = row['empname']
                        spaceforcename = row['spaceforce']
                        secid = row['secid']
                        x = row['x']
                        y = row['y']

                    empirecommand = ""
                    while empirecommand != "q" or empirecommand != "Q":
                        match empirecommand:
                            case ('n' | 'N'):
                                empirename = changeEmpireName(eid)
                            case ('f' | 'f'):
                                spaceforcename = changeSpaceForceName(eid)
                            case ('s' | 'S'):
                                secid = changeSecID(eid)
                            case ('x' | 'X'):
                                x = changeX(eid)
                            case ('y' | 'Y'):
                                y = changeY(eid)
                            case ('d' | 'D'): # Delete the empire.
                                 deleteEmpire(eid)
                            case ('q' | 'Q'):
                                main.menu()
                            case ('?' | ''):
                                func.clear()
                                print("")
                                art.cd(
                                    226, '', "\t\t\tEDIT EMPIRE INFORMATION", "", True)
                                print("")
                                # Empire Name
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "N", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Empire Name:\t", "", False)
                                art.cd(2, '', str(empirename), "", True)
                                # Space Force Name
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "F", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Space Force Name:\t", "", False)
                                art.cd(2, '', str(spaceforcename), "", True)
                                print("")
                                art.cd(1, '', "Not sure that the following are needed.", "", True)
                                # Empire SecID
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "S", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "SecID:\t\t", "", False)
                                art.cd(2, '', str(secid), "", True)
                                # X Coordinate
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "X", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "X Coordinate:\t", "", False)
                                art.cd(2, '', str(x), "", True)
                                # Y Coordinate
                                art.cd(5, '', "<", "", False)
                                art.cd('light_cyan', '', "Y", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd('light_cyan', '',
                                       "Y Coordinate:\t", "", False)
                                art.cd(2, '', str(y), "", True)
                                print()
                                art.cd(5, '', "<", "", False)
                                art.cd('226', '', "Q", "", False)
                                art.cd(5, '', "> ", "", False)
                                art.cd(2, '', "Quit Empire Editor", "", True)
                                print()
                            case _:
                                print("")
                                art.cd(
                                    1, '', "Command not found. Please try again.", 0, True)
                                print("")

                        print("")
                        art.cd(5, '', "[Empire Editor] ", '', False)
                        art.cd('light_cyan', '',
                               "Which attribute would you like to edit? ", 0, False)
                        art.cd(226, '', "[?]", '', False)
                        art.cd('light_cyan', '', ": ", 0, False)
                        empirecommand = input("")

                else:
                    print("")
                    art.cd(1, '', "Empire not found", '', True)
                    command = ""