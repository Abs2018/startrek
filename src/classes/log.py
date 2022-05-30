import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


class log():
    def __init__(self):
        pass

    def logAdd(self, logtype, log):
        connection = db.stdb()
        query = "INSERT INTO `logs` (`logtype`, `log`) VALUES ('" + \
            logtype+"', '"+log+"')"
        db.query(connection, query)

    def logShow(self):
        # Show today's log. # Create a file with log of daily events.
        print("")
        art.cd(10, '', "Show today's log? (", '', False)
        art.cd(11, '', "Y/N", '', False)
        art.cd(10, '', ") [", '', False)
        art.cd(14, '', "N", '', False)
        art.cd(10, '', "] ", '', False)
        command = input("")
        if command == "Y" or command == "y":
            # Open the log file and display it here.
            print("")
            art.cd(12, '', "\t\t\tCaptain's Log", '', True)
            print("")
            connection = db.stdb()
            query = "SELECT * FROM `logs` WHERE DATE(`createdate`) = CURDATE()"
            results = db.query(connection, query)
            for row in results:
                match row['logtype']:
                    case 'NEWPLAYER':
                        art.cd(11, '', str(row['createdate'])+"\t", '', False)
                        art.cd(10, '', row['log']+"\t", 0, True)
            print("")
        elif command == "N" or command == "" or command == "n":
            print("")
            art.cd(10, '', "Log skipped.", 0, True)
            print("")
