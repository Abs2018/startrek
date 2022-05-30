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

    def spacedock(self,playerinfo):
        # This is the spacedock menu.
        command = ""
        while command != "q":
            print("")
            print (13,'',"<",'',False)
            art.cd(11,'',"Stardock",'',False)
            art.cd(13,'',"> Where to? (",'',False)
            art.cd(11,'',"?=Help",'',False)
            art.cd(13,'',"): ",'',False)
            command = input("")
            match command:
                case "b": # Seedy singles bar
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"This is a rather seedy looking single's bar.")
                    print(Fore.GREEN+Style.BRIGHT+"Are you sure you want to go in there?")
                    command = input("")
                    if command == "y" or command == "Y":
                        print(Fore.CYAN+Style.BRIGHT+"You feel rather nervous as you enter this rather seedy establishment. But after a few drinks you begin to carouse with members of the opposite sex and you forget about your surroundings. You emerge from the place a few hours later with a nasty headache and you notice that your account on your VidCreditCard is much lower than when you entered.")
                    spacedock(player)
                case 'c': # CinePlex Videon Theaters
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"The Theaters are closed at the moment.")
                case 'g': # 2nd National Galactic Bank
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"The Theaters are closed at the moment.")
                case 'h': # Stellar Hardware Emporium
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"The Hardware Emporium hasn't opened yet.")
                case 'l': # Libram Universitatus
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"The Librum Universtatus is closed for renovations.")
                case 'p': # Federal Space Police HQ
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"The Police turn you away, saying they're too busy for you.")
                case 's': # Federation Shipyards
                    shipyards(path, slash, player)
                case 't': # Lost Trader's Tavern
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"The Tavern is closed roe a private party.")
                case 'u': # Underground
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"A shady doorway looks entirely uninviting. It's probably best to avoid it for now.")
                case "!": # Stardock help
                    pass
                case "r": # Go to your ship
                    player.whereami = "ship"
                    p.playersave(path,slash,player.userid,player.firstname,player.middlename,player.lastname,player.alignment,player.rank,player.branch,player.xp,player.kills,player.deaths,player.locationx,player.locationy,player.whereami,player.health,player.species,player.age,player.birthday,player.homeplanet,player.languages)
                    break
                case 'q': # Quit the whole game.
                    print(Fore.WHITE+Back.BLUE+Style.BRIGHT+"Live long and prosper.")
                    quit()
                case '?': # Help
                    print(Back.BLACK+Fore.RED+Style.BRIGHT+"<Help>")
                    print("")
                    print(Fore.GREEN+Style.BRIGHT+"    Obvious places to go are"+11,'',":")
                    print("")
                    print(13,''," <"+Fore.GREEN+Style.BRIGHT+"C"+13,'',"> "+Fore.CYAN+Style.BRIGHT+"The CinePlex Videon Theaters")
                    print(13,''," <"+Fore.GREEN+Style.BRIGHT+"G"+13,'',"> "+Fore.CYAN+Style.BRIGHT+"The 2nd National Galactic Bank")
                    print(13,''," <"+Fore.GREEN+Style.BRIGHT+"H"+13,'',"> "+Fore.CYAN+Style.BRIGHT+"The Stellar Hardware Emporium")
                    print(13,''," <"+Fore.GREEN+Style.BRIGHT+"L"+13,'',"> "+Fore.CYAN+Style.BRIGHT+"The Libram Universitatus")
                    print(13,''," <"+Fore.GREEN+Style.BRIGHT+"P"+13,'',"> "+Fore.CYAN+Style.BRIGHT+"The Federal Space Police HQ")
                    print(13,''," <"+Fore.GREEN+Style.BRIGHT+"S"+13,'',"> "+Fore.CYAN+Style.BRIGHT+"The Federation Shipyards")
                    print(13,''," <"+Fore.GREEN+Style.BRIGHT+"T"+13,'',"> "+Fore.CYAN+Style.BRIGHT+"The Lost Trader's Tavern")
                    print("")
                    print(13,''," <"+11,'',"!"+13,'',"> "+11,'',"Stardock Help")
                    print(13,''," <"+11,'',"R"+13,'',"> "+11,'',"Return to your ship and leave")
                    print("")
                    print(13,''," <"+Fore.RED+Style.BRIGHT+"Q"+13,'',"> "+Fore.RED+Style.BRIGHT+"Quit the game")
                case _: # Approximating what TW2002 does here.
                    rand = random.randrange(0,100)
                    if rand < 10:
                        print("")
                        print(Fore.CYAN+Style.BRIGHT+"As you wander about looking down dark corridors, you hear some noise behind you. You spin around to see who is approaching you, but everything goes dark as you are hit.")
                        print("")
                        print(Fore.CYAN+Style.BRIGHT+"You wake up a few hours later and find most of your money gone.")
                        # TO DO: Implement money or whatever disappearing.

                    else :
                        print("")
                        print(Fore.CYAN+Style.BRIGHT+"You wander about the port but find nothing but locked doors and deadends. You do notice some rather rough looking characters lurking about the place. Maybe its not such a good idea to wander about without knowing where it's safe to go?")




    # def eventHandler(self, playerinfo):
    #     match playerinfo.whereami:
    #         case 'station':

    #             print("You are on a space station.")
    #             command = input("What would you like to do? ")
    #         case 'ship':
    #             print("You are on a space ship.")
    #             command = input("What would you like to do? ")


