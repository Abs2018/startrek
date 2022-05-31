
                case 'e':  # Examine ship specs
                    art.cd(15, 4, "<Examine Ship Stats>")
                    print("")
                    art.cd(
                        2, "You call up the Ship Catalog and browse through the Starship specs.")
                    specs = ""
                    while specs != 'q':
                        print("")
                        print(
                            13, '', "Which ship are you interested in? (", '', False)
						art.cd(11, '', "?=List", '', False)
						art.cd(13, '', "): ", 0, True)
                        specs = input("")

                        match specs:
                            case '?':
                                # Show all the ships
                                # Get list of files from ship folder.
                                newpath = path + "ships"+slash+"classes"+slash
                                ships = os.listdir(newpath)
                                # loop through and create menu.
                                i = 1
                                for s in ships:
                                    file = newpath+s
                                    # NOTE: Need to store display name format in the ship class file.
                                    shipfilef = open(file, 'r')
                                    shipfile = shipfilef.readlines()
                                    shipfilef.close()
                                    shipname = shipfile[0].split(";")
                                    fore1 = shipname[0]
                                    back1 = shipname[1]
                                    style1 = shipname[2]
                                    match fore1:
                                        case 'bl':
                                            fore1 = Fore.BLACK
                                        case 'r':
                                            fore1 = Fore.RED
                                        case 'g':
                                            fore1 = Fore.GREEN
                                        case 'y':
                                            fore1 = Fore.YELLOW
                                        case 'b':
                                            fore1 = Fore.BLUE
                                        case 'm':
                                            fore1 = Fore.MAGENTA
                                        case 'c':
                                            fore1 = Fore.CYAN
                                        case 'w':
                                            fore1 = Fore.WHITE
                                        case '':
                                            pass
                                    match back1:
                                        case 'bl':
                                            back1 = Back.BLACK
                                        case 'r':
                                            back1 = Back.RED
                                        case 'g':
                                            back1 = Back.GREEN
                                        case 'y':
                                            back1 = Back.YELLOW
                                        case 'b':
                                            back1 = Back.BLUE
                                        case 'm':
                                            back1 = Back.MAGENTA
                                        case 'c':
                                            back1 = Back.CYAN
                                        case 'w':
                                            back1 = Back.WHITE
                                        case '':
                                            pass
                                    match style1:
                                        case 'd':
                                            style1 = Style.DIM
                                        case 'n':
                                            style1 = Style.NORMAL
                                        case 'b':
                                            style1 = Style.BRIGHT
                                        case 'r':
                                            style1 = Style.RESET_ALL
                                        case '':
                                            pass
                                    name = shipname[3]
                                    print(13, "<"+2, str(i)+13, "> " +
                                          fore1+back1+name, end="")
                                    i = i + 1
                                print("")
                                print(13, "<"+2, "Q"+13, "> "+2, "To Leave")

                            case 'q':
                                print(2, "You shut off the Vid Term.")
                            case _:
                                # Try and open ship file.
                                newpath = path + "ships"+slash+"classes"+slash
                                ships = os.listdir(newpath)
                                # loop through and create menu.
                                for s in ships:  # Split at the dash and match number.
                                    testcase = s.split("-")
                                    testcase = testcase[0]
                                    if str(testcase) == str(specs):
                                        # print(2,"Selected: \""+specs+"\" Current ship: "+testcase)
                                        # print(type(specs),type(testcase))
                                        file = newpath+s
                                        found = True
                                        break
                                    else:
                                        # print(2,"Selected: \""+specs+"\" Current ship: "+testcase)
                                        found = False
                                if found == True:
                                    print("")
                                    file = newpath+s
                                    # NOTE: Need to store display name format in the ship class file.
                                    shipclass = Ship.shipclassload(file)
                                    shipclass = sc.shipclass(shipclass[0], shipclass[1], shipclass[2], shipclass[3], shipclass[4], shipclass[5], shipclass[6], shipclass[7], shipclass[8], shipclass[9], shipclass[10], shipclass[11], shipclass[12], shipclass[13], shipclass[14], shipclass[15], shipclass[16], shipclass[17], shipclass[18], shipclass[19], shipclass[20], shipclass[21],
                                                             shipclass[22], shipclass[23], shipclass[24], shipclass[25], shipclass[26], shipclass[27], shipclass[28], shipclass[29], shipclass[30], shipclass[31], shipclass[32], shipclass[33], shipclass[34], shipclass[35], shipclass[36], shipclass[37], shipclass[38], shipclass[39], shipclass[40], shipclass[41], shipclass[42], shipclass[43], shipclass[44])

                                    # shipfile = open(file, 'r')
                                    # shipclass = []
                                    # shipclass = shipfile.read().splitlines()
                                    # Get the name and format.
                                    shipname = shipclass.shipclass.split(";")
                                    fore1 = shipname[0]
                                    back1 = shipname[1]
                                    style1 = shipname[2]

                                    match fore1:
                                        case 'bl':
                                            fore1 = Fore.BLACK
                                        case 'r':
                                            fore1 = Fore.RED
                                        case 'g':
                                            fore1 = Fore.GREEN
                                        case 'y':
                                            fore1 = Fore.YELLOW
                                        case 'b':
                                            fore1 = Fore.BLUE
                                        case 'm':
                                            fore1 = Fore.MAGENTA
                                        case 'c':
                                            fore1 = Fore.CYAN
                                        case 'w':
                                            fore1 = Fore.WHITE
                                        case '':
                                            pass
                                    match back1:
                                        case 'bl':
                                            back1 = Back.BLACK
                                        case 'r':
                                            back1 = Back.RED
                                        case 'g':
                                            back1 = Back.GREEN
                                        case 'y':
                                            back1 = Back.YELLOW
                                        case 'b':
                                            back1 = Back.BLUE
                                        case 'm':
                                            back1 = Back.MAGENTA
                                        case 'c':
                                            back1 = Back.CYAN
                                        case 'w':
                                            back1 = Back.WHITE
                                        case '':
                                            pass
                                    match style1:
                                        case 'd':
                                            style1 = Style.DIM
                                        case 'n':
                                            style1 = Style.NORMAL
                                        case 'b':
                                            style1 = Style.BRIGHT
                                        case 'r':
                                            style1 = Style.RESET_ALL
                                        case '':
                                            pass
                                    name = shipname[3]
                                    # Calculate ship cost.
                                    shipbasecost = int(shipclass.costofholdspace) + int(shipclass.costofdrive) + int(
                                        shipclass.costofcomputersystem) + int(shipclass.costofshipshull)
                                    # Clear the screen
                                    os.system('cls' if os.name ==
                                              'nt' else 'clear')
                                    # Does the ship have a photon torpedo launcher?
                                    if int(shipclass.photontorpedoesmax) > 0:
                                        ptlauncher = "Yes"
                                    else:
                                        ptlauncher = "No"
                                    # Print graphic
                                    artfile = path + "ships"+slash+"art"+slash+s+"-art"
                                    shipimage = Ship.shipclassimageload(
                                        artfile)
                                    print("")
                                    print("")
                                    # Print stats
                                    print(2, '', "    Basic Hold Cost"+11, '', ":   "+14, '', f"{shipclass.costofholdspace}"+2, '', "\t  Initial Holds"+11, '',
                                          ":   "+14, '', f"{shipclass.cargoholdsstart}"+2, '', "\t  Maximum Shields"+11, '', ":   "+14, '', f"{shipclass.shieldsmax}")
                                    print(2, '', "    Main Drive Cost"+11, '', ":   "+14, '', f"{shipclass.costofdrive}"+2, '', "\t   Max Fighters" +
                                          11, '', ":   "+14, '', f"{shipclass.fightersmax}"+2, '', "\t   Offensive Odds"+11, '', ":   "+14, '', f"N/A")
                                    print(2, '', "      Computer Cost"+11, '', ":   "+14, '', f"{shipclass.costofcomputersystem}"+2, '',
                                          "\t Turns Per Warp"+11, '', ":   "+14, '', f"N/A"+2, '', "\t   Defensive Odds"+11, '', ":   "+14, '', f"N/A")
                                    print(2, '', "     Ship Hull Cost"+11, '', ":   "+14, '', f"{shipclass.costofshipshull}"+2, '', "\t       Mine Max"+11, '',
                                          ":   "+14, '', f"{shipclass.minesmax}"+2, '', "\t       Beacon Max"+11, '', ":   "+14, '', f"{shipclass.markerbeaconsmax}")
                                    print(2, '', "     Ship Base Cost"+11, '', ":   "+14, '', str(shipbasecost)+2, '', "\t    Genesis Max"+11, '', ":   "+14,
                                          '', f"{shipclass.genesistorpedoes}"+2, '', "\t  Long Range Scan"+11, '', ":   "+14, '', f"{shipclass.cargoholdsstart}")
                                    print(2, '', "Max Figs Per Attack"+11, '', ":   "+14, '', f"{shipclass.fighterattackforce}"+2, '', "\tTranswarp Drive"+11, '',
                                          ":   "+14, '', f"{shipclass.transwarpdrive}"+2, '', "\t   Planet Scanner"+11, '', ":   "+14, '', f"{shipclass.planetscanner}")
                                    print(2, '', "      Maximum Holds"+11, '', ":   "+14, '', f"{shipclass.cargoholdsmax}"+2, '', "\tTransport Range"+11,
                                          '', ":   "+14, '', f"{shipclass.cargoholdsmax}"+2, '', "\t  Photon Missiles"+11, '', ":   "+14, '', ptlauncher)
                                elif found == False:
                                    print("")
                                    print(
                                        2, "The Vid Term doesn't recognize your choice. Try again.")

                                # If not exists, print "I can't seem to find that ship reference."
            match command:
                case 'p': # Buy class 0 items
                    pass
                case 'r': # Change ship registration
                    pass
                case '?': # Display menu
                    print("")
                    art.cd(2,'',"  The Federation Shipards"+11,'',":",0,True)
                    print("")
                    art.cd(13,''," <",'',False)
					art.cd(2,'',"B",'',False)
					art.cd(13,'',"> ",'',False)
					art.cd(14,'',"Buy a New Ship",0,True)

                    art.cd(13,''," <",'',False)
					art.cd(2,'',"S",'',False)
					art.cd(13,'',"> ",'',False)
					art.cd(14,'',"Sell Extra Ships",0,True)

                    art.cd(13,''," <",'',False)
					art.cd(2,'',"E",'',False)
					art.cd(13,'',"> ",'',False)
					art.cd(14,'',"Examine Ship Specs",0,True)

                    art.cd(13,''," <",'',False)
					art.cd(2,'',"P",'',False)
					art.cd(13,'',"> ",'',False)
					art.cd(14,'',"Buy Class 0 Items",0,True)

                    art.cd(13,''," <",'',False)
					art.cd(2,'',"R",'',False)
					art.cd(13,'',"> ",'',False)
					art.cd(14,'',"Change Ship Registration",0,True)

                    print("")
                    art.cd(13,''," <",'',False)
					art.cd(11,'',"!",'',False)
					art.cd(13,'',"> ",'',False)
					art.cd(11,'',"Shipyards Help",0,True)
                    art.cd(13,''," <",'',False)
					art.cd(11,'',"Q",'',False)
					art.cd(13,'',"> ",'',False)
					art.cd(11,'',"Leave the Shipyards",0,True)
                case '!': # Shipyards help
                    pass
                case 'q': # Leave the shipyards.
                    art.cd(2,"You leave the shipyards.",0,True)
                    break
                case _:
                    art.cd(2,"You can't seem to find anyone to talk to.",0,True)