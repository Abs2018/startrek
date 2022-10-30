
# This is the script that will edit a sector and all the things within it.

# Import the required modules.
from modules import db
from modules import art
from modules.menu.adm import main

def sectorMenu():
    # Row ??
    print("")
    print("")
    art.cd(5, '', "<", "", False)
    art.cd('226', '', "Q", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "Quit Sector Editor", "", True)
    # Footer
    art.cd("", "", "", "reset", True)


def menu():
    command = ""
    while command != "q":
        if command == "":
            print("")
            art.cd(5, '', "[Sector Editor] ", '', False)
            art.cd('light_cyan', '',
                   "[WIP] Which sector would you like to edit? ", 0, False)
            art.cd(226, '', "[?]", '', False)
            art.cd('light_cyan', '', ": ", 0, False)
            command = input(" ")

        match command:
            case ('?' | ''):
                sectorMenu()
            case ('q' | 'Q'):
                main.menu()