from modules import art
from classes import playerClass


class menus():
    def __init__(self):
        pass

    def gameStart(self):
        def displaymain():
            print("")
            art.cd(51, '', " ==-", '', False)
            art.cd(255, '', "- Star Trek -", '', False)
            art.cd(51, '', "-==", '', True)
            print("")
            art.cd(255, '', " P", '', False)
            art.cd(51, '', " - Play Star Trek", '', True)
            art.cd(255, '', " I", '', False)
            art.cd(51, '', " - Introduction and Help", '', True)
            art.cd(255, '', " S", '', False)
            art.cd(51, '', " - View Game Settings", '', True)
            art.cd(255, '', " H", '', False)
            art.cd(51, '', " - High Scores", '', True)
            art.cd(255, '', " M", '', False)
            art.cd(51, '', " - View Access Modes", '', True)
            art.cd(255, '', " Q", '', False)
            art.cd(51, '', " - Exit", '', True)
            print("")
        displaymain()
        command = ""
        while command != "q":
            art.cd(51, '', "Enter your choice: ", '', True)
            art.cd(255, '', "", '', False)
            command = input("")
            match command:
                case ('p' | 'P'):
                    # start()
                    command = 'q'
                case ('i' | 'I'):
                    pass
                case ('s' | 'S'):
                    pass
                case ('h' | 'H'):
                    from classes import highscores
                    hs = highscores.highScores()
                    hs.show()
                case ('m' | 'M'):
                    pass
                case ('q' | 'Q'):
                    print("")
                    art.cd(255, 4, "Live long and prosper.", 0, True)
                    print("")
                    quit()
                case ('?' | ''):
                    displaymain()

    def PlayerSetup():
        pass
