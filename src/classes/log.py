import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


class log():
    def __init__(self):
        pass

    def logShow(self):
        # Show today's log. # Create a file with log of daily events.
        print("")
        art.cd(2, '', "Show today's log? (", '', False)
        art.cd(3, '', "Y/N", '', False)
        art.cd(2, '', ") [", '', False)
        art.cd(14, '', "N", '', False)
        art.cd(2, '', "]", '', False)
        command = input("")
        if command == "Y":
            pass  # Open the log file and display it here.
        elif command == "N" or command == "" or command == "n":
            print("")
            art.cd(2, '', "Log skipped.", 0, True)
            print("")
