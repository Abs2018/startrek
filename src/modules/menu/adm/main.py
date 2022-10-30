# This is the admin.py main menu.

# Import the required modules.
from modules import db
from modules import art
import modules.menu.adm.bigbang as bigbang
from modules.menu.adm import sectors
from modules.menu.adm import editorEmpire
from modules import funcPlayer
from modules import funcShip
from modules import funcGalaxy
from modules import funcEmpires

def menu():
    print("")
    art.cd(226, '', "\t\t\tSTAR TREK GAME CONFIGURATION MENU", "", True)
    print("")
    menuitem = 0
    # Row 1
    art.cd(5, '', "<", "", False)
    art.cd('light_cyan', '', "B", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "The Big Bang\t", "", False)
    playercount = funcPlayer.anyplayers()
    menuitem = menuitem + 1
    if type(playercount) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "U", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "User Editor\t\t", "", End)

    shipcount = funcShip.anyships()
    menuitem = menuitem + 1
    if type(shipcount) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "S", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "Ship Editor\t\t", "", End)

    galrad = funcGalaxy.galaxyradius()
    # print("Galaxy Radius:"+galrad)
    menuitem = menuitem + 1
    if type(galrad) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "C", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "Sector Editor\t", "", End)
    # Row 2
    if type(galrad) == int:
        empirecount = funcEmpires.anyempires()
        menuitem = menuitem + 1
        if type(empirecount) == int:
            art.cd(5, '', "<", "", False)
            art.cd('light_cyan', '', "E", "", False)
            art.cd(5, '', "> ", "", False)
            if menuitem % 4 == 0:
                End = True
            else:
                End = False
            art.cd(2, '', "Empire Editor\t", "", End)

    menuitem = menuitem + 1
    if type(galrad) == int:
        art.cd(5, '', "<", "", False)
        art.cd('light_cyan', '', "G", "", False)
        art.cd(5, '', "> ", "", False)
        if menuitem % 4 == 0:
            End = True
        else:
            End = False
        art.cd(2, '', "Galaxy Browser\t", "", End)

    # Row ??
    print("")
    print("")
    art.cd(5, '', "<", "", False)
    art.cd('226', '', "Q", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "Quit Editor", "", True)
    # Footer
    art.cd("", "", "", "reset", True)

    command = ""
    while command != "q":
        art.cd('light_cyan', '', "Enter your choice ", 'reset', False)
        art.cd('226', '', "[?]", 'reset', False)
        art.cd('light_cyan', '', ": ", 'reset', False)
        command = input("")
        match command:
            case ('b' | 'B'):
                # The Big Bang
                bigbang.mainMenu()
                # This will display the menu once you leave the Big Bang Editor.
                menu()
            case ('c' | 'C'):
                # Sector viewer.
                sectors.menu()
            case ('e' | 'E'):
                # Empire editor.
                editorEmpire.menu()
            case ('g' | 'G'):
                # Galaxy Viewer.
                galaxymenu(0, 0)
            case ('s' | 'S'):
                # Ship viewer.
                ship_menu()
            case ('u' | 'U'):
                # User viewer.
                user_menu()
            case ('?' | ''):
                adm_main_menu()
            case ('q' | 'Q'):
                print("")
                art.cd(0, 196, "  Live long and prosper  ", 'reset', True)
                print("")
                quit()
            case _:
                art.cd(1, '', 'Command not found. Please try again.',
                       "reset", True)
                print("")

