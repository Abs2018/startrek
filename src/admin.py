# This is the admin app.

# Import the required modules.
import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art
from modules import setup
from modules import bigbang as bb


# import cgi


connection = db.stdb()
if connection == "FALSE":
    # The database has not been installed. Display setup menu.
    art.cd(22, '', "First time setup detected.", "reset", True)
    setup.setup()

# Continue to menu.
'''
Characters from https://en.wikipedia.org/wiki/Code_page_437

░ ▒ ▓ █ ▄ ▀ ■ ▌▐ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐ └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧ ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌
· ∙ ° ° • . *

┌─┬─┐
│ │ │
├─┼─┤
└─┴─┘
'''


def adm_main_menu():
    print("")
    art.cd(226, '', "\tSTAR TREK GAME CONFIGURATION MENU", "", True)
    print("")
    # Row 1
    art.cd(5, '', "\t<", "", False)
    art.cd('light_cyan', '', "B", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "The Big Bang", "", False)

    art.cd(5, '', "\t<", "", False)
    art.cd('light_cyan', '', "S", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "Sector Editor", "", True)

    # Row ??
    print("")
    art.cd(5, '', "\t<", "", False)
    art.cd('226', '', "Q", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(2, '', "Quit Editor", "", True)
    # Footer
    art.cd("", "", "", "reset", True)


# The Main Menu
adm_main_menu()
command = ""
while command != "q":
    art.cd('light_cyan', '', "Enter your choice ", 'reset', False)
    art.cd('226', '', "[?]", 'reset', False)
    art.cd('light_cyan', '', ": ", 'reset', False)
    command = input("")
    match command:
        case ('b' | 'B'):
            # The Big Bang
            bb.bb_main_menu()
            # This will display the menu once you leave the Big Bang Editor.
            adm_main_menu()
        case ('s' | 'S'):
            # Sector viewer.
            pass
        case ('?' | ''):
            adm_main_menu()
        case ('q' | 'Q'):
            print("")
            art.cd(0, 196, "  Live long and prosper  ", 'reset', True)
            print("")
            quit()
        case _:
            art.cd(1, '', 'Command not found. Please try again.', "reset", True)
            print("")
