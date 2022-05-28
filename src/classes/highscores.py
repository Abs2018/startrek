import mysql.connector
from mysql.connector import Error
from modules import db
from modules import art


class highScores():
    def __init__(self):
        pass

    def show(self):
        print("")
        art.cd(51, '', "\t\t==-", '', False)
        art.cd(255, '', "- High Scores -", '', False)
        art.cd(51, '', "-==", '', True)
        print("")
        connection = db.stdb()
        query = "select * from `highscores`"
        highscorecount = db.query(connection, query)
        if highscorecount == 0:
            # Display empty table message.
            for i in range(1, 11):
                if i < 10:
                    prefix = " "+str(i)+". "
                else:
                    prefix = str(i)+". "
                art.cd(2, '', prefix, '', False)
                art.cd(51, '', "Empty\t\t\t\t\t", '', False)
                art.cd(3, '', "0", '', True)
            print("")
        else:
            i = 1
            for row in highscorecount:
                if i < 10:
                    prefix = " "+str(i)+". "
                else:
                    prefix = str(i)+". "

                connection = db.stdb()
                query = "select `name` from `players` where `pid` = '" + \
                    str(row['pid'])+"'"
                playerresults = db.query(connection, query)
                for prow in playerresults:
                    if prow['name'] != '':
                        name = prow['name']
                    else:
                        name = "Player not found"
                # Print results
                art.cd(2, '', prefix, '', False)
                art.cd(51, '', name+"\t\t\t\t\t", '', False)
                art.cd(3, '', str(row['score']), '', True)
                i = i + 1
            connection = db.stdb()
            query = "select * from `highscores`"
            highscorecount = db.rowcount(connection, query)
            if highscorecount <= 10:
                # rangestart = 10 - highscorecount
                # print(rangestart)
                highscorecount = highscorecount + 1
                for i in range(highscorecount, 11):
                    if i < 10:
                        prefix = " "+str(i)+". "
                    else:
                        prefix = str(i)+". "
                    art.cd(2, '', prefix, '', False)
                    art.cd(51, '', "Empty\t\t\t\t\t", '', False)
                    art.cd(3, '', "0", '', True)
                print("")
