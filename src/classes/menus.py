import random
from classes import player
from modules import art
from classes import playerClass
from classes import portClass
from classes import shipClass
portClass = portClass.portClass()
playerClass = playerClass.player()
shipClass = shipClass.shipClass()


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

    def portmenu(self, portinfo, playerinfo):
        command = ""
        while command != "q":
            print("")
            art.cd(13, '', "<", '', False)
            art.cd(11, '', portinfo.portname, '', False)
            art.cd(13, '', "> Where to? (", '', False)
            art.cd(11, '', "?=Help", '', False)
            art.cd(13, '', "): ", '', False)
            portattributes = portClass.portAttributes(portinfo.portclass)
            # print(portattributes)
            command = input("")
            match command:
                case ("b" | "B"):  # Seedy singles bar
                    if portattributes["bar"] == 1:
                        print("")
                        art.cd(
                            10, '', "This is a rather seedy looking single's bar.", 0, True)
                        art.cd(
                            10, '', "Are you sure you want to go in there?", 0, True)
                        command = input("")
                        if command == "y" or command == "Y":
                            art.cd(123, '', "You feel rather nervous as you enter this rather seedy establishment. But after a few drinks you begin to carouse with members of the opposite sex and you forget about your surroundings. You emerge from the place a few hours later with a nasty headache and you notice that your account on your VidCreditCard is much lower than when you entered.", 0, True)
                        # spacedock(player)
                    else:
                        print("")
                        art.cd(9, '', "This port does not have a bar.", 0, True)
                case ("c" | "C"):  # CinePlex Videon Theaters
                    if portattributes["theater"] == 1:
                        print("")
                        art.cd(
                            10, '', "The Theaters are closed at the moment.", 0, True)
                    else:
                        print("")
                        art.cd(
                            9, '', "This port does not have a holotheater.", 0, True)
                case ("g" | "G"):  # 2nd National Galactic Bank
                    if portattributes["bank"] == 1:
                        print("")
                        art.cd(
                            10, '', "The Bank is closed at the moment. You suddenly find yourself wishing that you worked banker's hours.", 0, True)
                    else:
                        print("")
                        art.cd(9, '', "This port does not have a bank.", 0, True)
                case ("h" | "H"):  # Stellar Hardware Emporium
                    if portattributes["techdealer"] == 1:
                        print("")
                        art.cd(
                            10, '', "The Hardware Emporium hasn't opened yet.", 0, True)
                    else:
                        print("")
                        art.cd(
                            9, '', "This port does not have a HArdware Emporium.", 0, True)
                case ("l" | "L"):  # Libram Universitatus
                    if portattributes["library"] == 1:
                        print("")
                        art.cd(
                            10, '', "The Librum Universtatus is closed for renovations.", 0, True)
                    else:
                        print("")
                        art.cd(9, '', "This port does not have a Library.", 0, True)
                case ("p" | "P"):  # Federal Space Police HQ
                    if portattributes["police"] == 1:
                        print("")
                        art.cd(
                            10, '', "The Police turn you away, saying they're too busy for you.", 0, True)
                    else:
                        print("")
                        art.cd(
                            9, '', "This port does not have a Police Station.", 0, True)
                case ("s" | "S"):  # Federation Shipyards
                    if portattributes["shipyards"] == 1:
                        menus.shipyards(self, portinfo, playerinfo)

                    else:
                        print("")
                        art.cd(
                            9, '', "This port does not have a shipyard.", 0, True)
                case ("t" | "T"):  # Lost Trader's Tavern
                    if portattributes["tavern"] == 1:
                        print("")
                        art.cd(
                            10, '', "The Tavern is closed for a private party.", 0, True)
                    else:
                        print("")
                        art.cd(9, '', "This port does not have a Tavern.", 0, True)
                case ("u" | "U"):  # Underground
                    if portattributes["blackmarket"] == 1:
                        print("")
                        art.cd(
                            10, '', "A shady doorway looks entirely uninviting. It's probably best to avoid it for now.", 0, True)
                    else:
                        print("")
                        art.cd(
                            9, '', "With all the security personnel on this port, you are not surprised that you can't find a black market here.", 0, True)
                case ("r" | "R"):  # Return to ship
                    # playerinfo = player.player(pid)
                    # print(playerinfo.pid)
                    playerinfo.whereami = playerClass.changewhereami(
                        playerinfo.pid, "ship")
                    break
                case ("q" | "Q"):  # Quit the whole game.
                    print("")
                    art.cd(255, 27, "Live long and prosper.", 0, True)
                    print("")
                    quit()

                case '?':  # Help
                    print("")
                    art.cd(196, 232, "<Help>", 0, True)
                    print("")
                    art.cd(10, '', "    Obvious places to go are", 0, False)
                    art.cd(11, '', ":", '', True)
                    print("")
                    if portattributes["theater"] == 1:
                        art.cd(13, '', " <", '', False)
                        art.cd(10, '', "C", '', False)
                        art.cd(13, '', "> ", '', False)
                        art.cd(123, '', "The CinePlex Videon Theaters", 0, True)

                    if portattributes["bank"] == 1:
                        art.cd(13, '', " <", '', False)
                        art.cd(10, '', "G", '', False)
                        art.cd(13, '', "> ", '', False)
                        art.cd(123, '', "The 2nd National Galactic Bank", 0, True)

                    if portattributes["techdealer"] == 1:
                        art.cd(13, '', " <", '', False)
                        art.cd(10, '', "H", '', False)
                        art.cd(13, '', "> ", '', False)
                        art.cd(123, '', "The Stellar Hardware Emporium", 0, True)

                    if portattributes["library"] == 1:
                        art.cd(13, '', " <", '', False)
                        art.cd(10, '', "L", '', False)
                        art.cd(13, '', "> ", '', False)
                        art.cd(123, '', "The Libram Universitatus", 0, True)

                    if portattributes["police"] == 1:
                        art.cd(13, '', " <", '', False)
                        art.cd(10, '', "P", '', False)
                        art.cd(13, '', "> ", '', False)
                        art.cd(123, '', "The Federal Space Police HQ", 0, True)

                    if portattributes["shipyards"] == 1:
                        art.cd(13, '', " <", '', False)
                        art.cd(10, '', "S", '', False)
                        art.cd(13, '', "> ", '', False)
                        art.cd(123, '', "The Federation Shipyards", 0, True)

                    if portattributes["tavern"] == 1:
                        art.cd(13, '', " <", '', False)
                        art.cd(10, '', "T", '', False)
                        art.cd(13, '', "> ", '', False)
                        art.cd(123, '', "The Lost Trader's Tavern", 0, True)

                    print("")
                    art.cd(13, '', " <", '', False)
                    art.cd(11, '', "!", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "Port Help", 0, True)

                    art.cd(13, '', " <", '', False)
                    art.cd(11, '', "R", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "Return to your ship and leave", 0, True)
                    print("")
                    art.cd(13, '', " <", '', False)
                    art.cd(196, '', "Q", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(196, '', "Quit the game", 0, True)
                case _:  # Approximating what TW2002 does here.
                    rand = random.randrange(0, 100)
                    if rand < 10:
                        print("")
                        art.cd(123, '', "As you wander about looking down dark corridors, you hear some noise behind you. You spin around to see who is approaching you, but everything goes dark as you are hit.", 0, True)
                        print("")
                        art.cd(
                            123, '', "You wake up a few hours later and find most of your money gone.", 0, True)
                        # TO DO: Implement money or whatever disappearing.

                    else:
                        print("")
                        art.cd(123, '', "You wander about the port but find nothing but locked doors and deadends. You do notice some rather rough looking characters lurking about the place. Maybe its not such a good idea to wander about without knowing where it's safe to go?", 0, True)

    def shipyards(self, portinfo, playerinfo):
        art.shipyards()
        command = ""
        while command != "q" or command != "Q":
            print("")
            art.cd(13, '', "<", '', False)
            art.cd(11, '', "Shipyards", '', False)
            art.cd(13, '', "> Your option? (", '', False)
            art.cd(11, '', "?=Help", '', False)
            art.cd(13, '', "): ", 0, True)
            command = input("")
            match command:
                case ('b' | 'B'):  # Buy a new ship
                    pass
                case ('s' | 'S'):  # Sell extra ships
                    pass
                case ('e' | 'E'):  # Examine ship specs
                    art.cd(15, 4, "<Examine Ship Stats>", 0, True)
                    print("")
                    art.cd(
                        2, '', "You call up the Ship Catalog and browse through the Starship specs.", 0, True)
                    specs = ""
                    while specs != 'q':
                        print("")
                        art.cd(
                            13, '', "Which ship are you interested in? (", '', False)
                        art.cd(11, '', "?=List", '', False)
                        art.cd(13, '', "): ", 0, True)
                        specs = input("")
                        match specs:
                            case '?':
                                shipClass.shipClassesView()
                            case ('q' | 'Q'):
                                print("")
                                art.cd(
                                    2, '', "You shut off the Vid Term.", 0, True)
                            case _:
                                shipClass.shipClassView(specs)

                case ('p' | 'P'):  # Buy class 0 items
                    pass
                case ('r' | 'R'):  # Change ship registration
                    pass
                case '?':  # Display menu
                    print("")
                    art.cd(2, '', "  The Federation Shipards", '', False)
                    art.cd(11, '', ":", 0, True)
                    print("")
                    art.cd(13, '', " <", '', False)
                    art.cd(2, '', "B", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(14, '', "Buy a New Ship", 0, True)

                    art.cd(13, '', " <", '', False)
                    art.cd(2, '', "S", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(14, '', "Sell Extra Ships", 0, True)

                    art.cd(13, '', " <", '', False)
                    art.cd(2, '', "E", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(14, '', "Examine Ship Specs", 0, True)

                    art.cd(13, '', " <", '', False)
                    art.cd(2, '', "P", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(14, '', "Buy Class 0 Items", 0, True)

                    art.cd(13, '', " <", '', False)
                    art.cd(2, '', "R", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(14, '', "Change Ship Registration", 0, True)

                    print("")
                    art.cd(13, '', " <", '', False)
                    art.cd(11, '', "!", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "Shipyards Help", 0, True)
                    art.cd(13, '', " <", '', False)
                    art.cd(11, '', "Q", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "Leave the Shipyards", 0, True)
                case '!':  # Shipyards help
                    pass
                case ('q' | 'Q'):  # Leave the shipyards.
                    print("")
                    art.cd(2, '', "You leave the shipyards.", 0, True)
                    break
                case _:
                    print("")
                    art.cd(
                        2, '', "You can't seem to find anyone to talk to.", 0, True)

    def shipmenu(self, shipinfo, playerinfo):
        command = ""
        while command != "q":
            print("")
            art.cd(13, '', "Command [", '', False)
            art.cd(14, '', str(playerinfo.locationx), '', False)
            art.cd(13, '', ",", '', False)
            art.cd(14, '', str(playerinfo.locationy), '', False)
            art.cd(13, '', "] (", '', False)
            art.cd(11, '', "?=Help", '', False)
            art.cd(13, '', "): ", '', False)
            command = input("")
            match command:
                # Navigation Column
                case ("d" | "D" | ''):  # Display Sector Summary
                    pass
                case ("p" | "P"):  # Land on Port
                    portClass.portDock(playerinfo)
                    break
                case ("m" | "M"):  # Move to a sector
                    pass
                case ("o" | "O"):  # Orbit a planet
                    pass
                case ("s" | "S"):  # Long Range Scan
                    pass
                case ("r" | "R"):  # Release Beacon
                    pass
                case ("w" | "W"):  # Tow Spacecraft
                    pass
                case ("n" | "N"):  # Move to NavPoint
                    pass
                case ("q" | "Q"):  # Quit the whole game.
                    print("")
                    art.cd(255, 27, "Live long and prosper.", 0, True)
                    print("")
                    quit()
                # Computer Column
                case ("c" | "C"):  # Onboard Computer
                    pass
                case ("x" | "X"):  # Transporter Pad
                    pass
                case ("i" | "I"):  # Ship Information
                    pass
                case ("t" | "T"):  # Corporate Menu
                    pass
                case ("u" | "U"):  # Use Genesis Torpedo
                    pass
                case ("j" | "J"):  # Jettison Cargo
                    pass
                case ("b" | "B"):  # Inderdict Control
                    pass
                case "!":  # Main Menu Help
                    pass
                case ("z" | "Z"):  # Documentation
                    pass
                # Tactical Column
                case ("a" | "A"):  # Attack Enemy Ship
                    pass
                case ("e" | "E"):  # Subspace Etherprobes
                    pass
                case ("f" | "F"):  # Take or Leave Fighters
                    pass
                case ("g" | "G"):  # Show Deployed Fighters
                    pass
                case ("h" | "H"):  # Handle Space Mines
                    pass
                case ("k" | "K"):  # Show Space Mines
                    pass
                case ("l" | "L"):  # Starport Constructionl
                    pass
                case ("y" | "Y"):  # Set Navpoints
                    pass
                case ("v" | "V"):  # View Game Status
                    pass

                case '?':  # Help
                    print("")
                    art.cd(9, 0, "<Help>", 0, True)
                    print("")
                    art.cd(2, '', "???????????????????????????????????????????????????????????????????????????????????????????????? ", 0, False)
                    art.cd(11, '', "STAR TREK", 0, False)
                    art.cd(2, '', " ????????????????????????????????????????????????????????????????????????????????????????????????", 0, True)

                    # Row 1
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', "\tNavigation", 0, False)
                    art.cd(13, '', "\t\tComputer", 0, False)
                    art.cd(13, '', "\t      Tactical", 0, False)
                    art.cd(2, '', "            ???", 0, True)
                    # Row 2
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(11, '', "\t=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(11, '', "\t\t=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(11, '', "\t      =", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "-", 0, False)
                    art.cd(11, '', "=", 0, False)
                    art.cd(2, '', "            ???", 0, True)
                    # Row 3
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "D", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Display Sector", 0, False)
                    art.cd(13, '', "    <", '', False)
                    art.cd(10, '', "C", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Onboard Computer", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "A", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Attack Enemy Ship", 0, False)
                    art.cd(2, '', "       ???", 0, True)
                    # Row 4
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "P", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Port and Trade", 0, False)
                    art.cd(13, '', "    <", '', False)
                    art.cd(10, '', "X", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Transporter Pad", 0, False)
                    art.cd(13, '', "  <", '', False)
                    art.cd(10, '', "E", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Sub-space EtherProbe", 0, False)
                    art.cd(2, '', "    ???", 0, True)
                    # Row 4
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "M", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Move to a Sector ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "I", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Ship Information", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "F", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Take or Leave Fighters ", 0, False)
                    art.cd(2, '', " ???", 0, True)
                    # Row 5
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "O", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Orbit a Planet   ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "T", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Corporate Menu  ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "G", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Show Deployed Fighters ", 0, False)
                    art.cd(2, '', " ??? ", 0, True)
                    # Row 6
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "S", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Long Range Scan  ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "U", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Use Genesis Torp", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "H", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Handle Space Mines     ", 0, False)
                    art.cd(2, '', " ???", 0, True)
                    # Row 7
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "R", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Release Beacon   ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "J", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Jettison Cargo  ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "K", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Show Deployed Mines    ", 0, False)
                    art.cd(2, '', " ???", 0, True)
                    # Row 8
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "W", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Tow Spacecraft   ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "B", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Interdict Ctrl  ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "L", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Starport Construction  ", 0, False)
                    art.cd(2, '', " ???", 0, True)
                    # Row 9
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "N", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Move to NavPoint ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "!", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "Main Menu Help  ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(10, '', "Y", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(123, '', "Set NavPoints          ", 0, False)
                    art.cd(2, '', " ???", 0, True)
                    # Row 10
                    art.cd(2, '', "??? ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(11, '', "Q", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "Quit and Exit    ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(11, '', "Z", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "Star Trek Docs  ", 0, False)
                    art.cd(13, '', " <", '', False)
                    art.cd(11, '', "V", '', False)
                    art.cd(13, '', "> ", '', False)
                    art.cd(11, '', "View Game Status       ", 0, False)
                    art.cd(2, '', " ???", 0, True)
                    # Row 11
                    art.cd(
                        2, '', "?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????", 0, True)

                case _:
                    print("")
                    art.cd(
                        9, '', "I'm unfamiliar with that command.", 0, True)
