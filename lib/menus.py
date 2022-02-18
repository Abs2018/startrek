from colorama import init, Style, Fore, Back
from lib import art
#import screens
init(autoreset=True)

def main():
	print("")
	print(Fore.CYAN+Style.BRIGHT+" ==-"+Fore.WHITE+Style.BRIGHT+"- Star Trek -"+Fore.CYAN+Style.BRIGHT+"-==")
	print("")
	print(Fore.WHITE+Style.BRIGHT+" P"+Fore.CYAN+Style.BRIGHT+" - Play Star Trek")
	print(Fore.WHITE+Style.BRIGHT+" I"+Fore.CYAN+Style.BRIGHT+" - Introduction and Help")
	print(Fore.WHITE+Style.BRIGHT+" S"+Fore.CYAN+Style.BRIGHT+" - View Game Settings")
	print(Fore.WHITE+Style.BRIGHT+" H"+Fore.CYAN+Style.BRIGHT+" - High Scores")
	print(Fore.WHITE+Style.BRIGHT+" M"+Fore.CYAN+Style.BRIGHT+" - View Access Modes")
	print(Fore.WHITE+Style.BRIGHT+" Q"+Fore.CYAN+Style.BRIGHT+" - Exit")
	print("")
	command = ""
	while command != "q":
		print(Fore.CYAN+Style.BRIGHT+"Enter your choice: "+Fore.WHITE)
		command = input("")
		match command:
			case ('p'|'P'):
				start()
			case ('i'|'I'):
				pass
			case ('s'|'S'):
				pass
			case ('h'|'H'):
				pass
			case ('m'|'M'):
				pass
			case ('q'|'Q'):
				art.cd("w","b","b","Live long and prosper.")
				quit()

def start():
	#
	# Start the game loop.
	#

	# Show today's log. # Create a file with log of daily events.
	print("")
	print(Fore.GREEN+Style.BRIGHT+"Show today's log? ("+Fore.YELLOW+Style.BRIGHT+"Y/N"+Fore.GREEN + ") ["+Fore.CYAN+Style.BRIGHT+"N"+Fore.GREEN+Style.BRIGHT+"]")
	command = input("")
	if command == "Y":
		pass # Open the log file and display it here.
	elif command == "N" or command == "" or command == "n":
		print("")
		print(Fore.GREEN+Style.BRIGHT+"Log skipped.")

	# Check to see if a player exists. If not, go through setup. If so, then call the game.
	isplayer = gf.gamefoldercheck(path,"player")
	fname=""
	mname=""
	lname=""
	option = ""
	if isplayer == "No player found":
		print("")
		print(Fore.GREEN+Style.BRIGHT+"You were not found in the player database.")
		print(Fore.WHITE+Style.BRIGHT+Back.BLUE+"Would you like to start a new character in this game? (Type "+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+"Y"+Fore.WHITE+Style.BRIGHT+Back.BLUE+" or "+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+"N"+Fore.WHITE+Style.BRIGHT+Back.BLUE+")"+Style.RESET_ALL+Fore.CYAN)
		command = input("")
		if command == "y" or command == "Y" or command == "":
			# Create the player.
			print("")
			print (Fore.YELLOW+Style.BRIGHT+"Great! "+Fore.CYAN+Style.BRIGHT+"Let's get some paperwork out of the way.")
			print("")
			print(Fore.CYAN+Style.BRIGHT+"What is your first name? "+Fore.WHITE+Style.BRIGHT)
			fname = input("")
			print(Fore.CYAN+Style.BRIGHT+"If you have a middle name, let me know. Press 'Enter' to skip. "+Fore.WHITE+Style.BRIGHT)
			mname = input("")
			print(Fore.CYAN+Style.BRIGHT+"Last, but not least, what is your last name? "+Fore.WHITE+Style.BRIGHT)
			lname = input("")
			branch = ""
			while branch == "":
				print(Fore.CYAN+Style.BRIGHT+"Which branch of service are you most interested in? ("+Fore.YELLOW+Style.BRIGHT+"Command"+Fore.CYAN+Style.BRIGHT+", "+Fore.BLUE+"Sciences"+Fore.CYAN+Style.BRIGHT+", or "+Fore.RED+"Operations"+Fore.CYAN+Style.BRIGHT+") "+Fore.WHITE)
				branch = input("")
				match branch:
					case "Command":
						branch = "Command"
					case "command":
						branch = "Command"
					case "Sciences":
						branch = "Sciences"
					case "sciences":
						branch = "Sciences"
					case "Operations":
						branch = "Operations"
					case "operations":
						branch = "Operations"
					case _:
						branch=""
			# Save the player name.
			print("")
			print(Fore.CYAN+Style.BRIGHT+"Give me a moment to sign you in...Okay, you're all set!")
			userid="1"
			alignment = "Federation"
			rank = 1
			xp = 0
			kills = 0
			deaths = 0
			locationx = 0
			locationy = 0
			whereami = "station"
			health = 100
			species = "Human"
			age = 22
			birthday = "24/04"
			homeplanet = "Earth"
			languages = "English"
			p.playercreate(path,slash,userid,fname,mname,lname,alignment,rank,branch,xp,kills,deaths,locationx,locationy,whereami,health,species,age,birthday,homeplanet,languages)
		elif command == "N" or command == "n":
			print(Fore.GREEN+Style.BRIGHT+"Maybe next time...")
			quit()
	# Instantiate player
	player = p.playerload(path,slash)
	player = pc.person(player[0],player[1],player[2],player[3],player[4],player[5],player[6],player[7],player[8],player[9],player[10],player[11],player[12],player[13],player[14],player[15],player[16],player[17],player[18])
	#print(Fore.GREEN+Style.BRIGHT+f"Welcome to the {player.alignment}, {player.rank} {player.lastname}! {player.branch} was a wise choice! While your experience may be {player.xp}, I'm sure you'll rank up in no time. Currently, you are in sector {player.locationx}, {player.locationy}. I am sure that you are eager to get started on your journey. You seem pretty healthy ({player.health}) for a {player.species}. Try not to miss {player.homeplanet}. Feel free to explore spacedock, or head over to your ship. If you ever need help, you can get it by pressing the '?' key. There are many here on this {player.whereami} who speak {player.languages}.")

	# Present the game menu
	print("")
	while command != "q":
		match command:
			case 'q': # Quit the whole game.
				art.cd("w","b","b","Live long and prosper.")
				quit()
			case _:
				if player.whereami == "station":
					if player.locationx == "0" and player.locationy == "0":
						m.spacedock(path,slash,player)
				elif player.whereami == "ship":
					m.playership(path,slash,player)
				elif player.whereami == "planet":
					pass




'''
def spacedock(path,slash,player):
	# This is the spacedock menu.
	command = ""
	while command != "q":
		print("")
		print (Fore.MAGENTA+Style.BRIGHT+"<"+Fore.YELLOW+Style.BRIGHT+"Stardock"+Fore.MAGENTA+Style.BRIGHT+"> Where to? ("+Fore.YELLOW+Style.BRIGHT+"?=Help"+Fore.MAGENTA+Style.BRIGHT+"): ")
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
				print(Fore.GREEN+Style.BRIGHT+"    Obvious places to go are"+Fore.YELLOW+Style.BRIGHT+":")
				print("")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"C"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"The CinePlex Videon Theaters")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"G"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"The 2nd National Galactic Bank")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"H"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"The Stellar Hardware Emporium")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"L"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"The Libram Universitatus")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"P"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"The Federal Space Police HQ")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"S"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"The Federation Shipyards")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"T"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"The Lost Trader's Tavern")
				print("")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.YELLOW+Style.BRIGHT+"!"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.YELLOW+Style.BRIGHT+"Stardock Help")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.YELLOW+Style.BRIGHT+"R"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.YELLOW+Style.BRIGHT+"Return to your ship and leave")
				print("")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.RED+Style.BRIGHT+"Q"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.RED+Style.BRIGHT+"Quit the game")
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

def shipyards(path,slash,player):
	screens.shipyards()
	command = ""
	while command != "q":
		print("")
		print (Fore.MAGENTA+Style.BRIGHT+"<"+Fore.YELLOW+Style.BRIGHT+"Shipyards"+Fore.MAGENTA+Style.BRIGHT+"> Your option? ("+Fore.YELLOW+Style.BRIGHT+"?=Help"+Fore.MAGENTA+Style.BRIGHT+"): ")
		command = input("")
		match command:
			case 'b': # Buy a new ship
				pass
			case 's': # Sell extra ships
				pass
			case 'e': # Examine ship specs
				print(Fore.WHITE+Back.BLUE+"<Examine Ship Stats>")
				print("")
				print(Fore.GREEN+"You call up the Ship Catalog and browse through the Starship specs.")
				specs = ""
				while specs != 'q':
					print("")
					print (Fore.MAGENTA+Style.BRIGHT+"Which ship are you interested in? ("+Fore.YELLOW+Style.BRIGHT+"?=List"+Fore.MAGENTA+Style.BRIGHT+"): ")
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
								print(Fore.MAGENTA+"<"+Fore.GREEN+str(i)+Fore.MAGENTA+"> "+fore1+back1+name,end="")
								i = i + 1
							print("")
							print(Fore.MAGENTA+"<"+Fore.GREEN+"Q"+Fore.MAGENTA+"> "+Fore.GREEN+"To Leave")

						case 'q':
							print(Fore.GREEN+"You shut off the Vid Term.")
						case _:
							# Try and open ship file.
							newpath = path + "ships"+slash+"classes"+slash
							ships = os.listdir(newpath)
							# loop through and create menu.
							for s in ships: # Split at the dash and match number.
								testcase = s.split("-")
								testcase = testcase[0]
								if str(testcase) == str(specs):
									#print(Fore.GREEN+"Selected: \""+specs+"\" Current ship: "+testcase)
									#print(type(specs),type(testcase))
									file = newpath+s
									found = True
									break
								else:
									#print(Fore.GREEN+"Selected: \""+specs+"\" Current ship: "+testcase)
									found = False
							if found == True:
								print("")
								file = newpath+s
								# NOTE: Need to store display name format in the ship class file.
								shipclass = Ship.shipclassload(file)
								shipclass = sc.shipclass(shipclass[0],shipclass[1],shipclass[2],shipclass[3],shipclass[4],shipclass[5],shipclass[6],shipclass[7],shipclass[8],shipclass[9],shipclass[10],shipclass[11],shipclass[12],shipclass[13],shipclass[14],shipclass[15],shipclass[16],shipclass[17],shipclass[18],shipclass[19],shipclass[20],shipclass[21],shipclass[22],shipclass[23],shipclass[24],shipclass[25],shipclass[26],shipclass[27],shipclass[28],shipclass[29],shipclass[30],shipclass[31],shipclass[32],shipclass[33],shipclass[34],shipclass[35],shipclass[36],shipclass[37],shipclass[38],shipclass[39],shipclass[40],shipclass[41],shipclass[42],shipclass[43],shipclass[44])


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
								shipbasecost = int(shipclass.costofholdspace) + int(shipclass.costofdrive) + int(shipclass.costofcomputersystem) + int(shipclass.costofshipshull)
								os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
								# Does the ship have a photon torpedo launcher?
								if int(shipclass.photontorpedoesmax) > 0:
									ptlauncher = "Yes"
								else:
									ptlauncher = "No"
								# Print graphic
								artfile = path + "ships"+slash+"art"+slash+s+"-art"
								shipimage = Ship.shipclassimageload(artfile)
								print("")
								print("")
								# Print stats
								print(Fore.GREEN+Style.BRIGHT+"    Basic Hold Cost"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.costofholdspace}"+Fore.GREEN+Style.BRIGHT+"\t  Initial Holds"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.cargoholdsstart}"+Fore.GREEN+Style.BRIGHT+"\t  Maximum Shields"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.shieldsmax}")
								print(Fore.GREEN+Style.BRIGHT+"    Main Drive Cost"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.costofdrive}"+Fore.GREEN+Style.BRIGHT+"\t   Max Fighters"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.fightersmax}"+Fore.GREEN+Style.BRIGHT+"\t   Offensive Odds"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"N/A")
								print(Fore.GREEN+Style.BRIGHT+"      Computer Cost"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.costofcomputersystem}"+Fore.GREEN+Style.BRIGHT+"\t Turns Per Warp"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"N/A"+Fore.GREEN+Style.BRIGHT+"\t   Defensive Odds"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"N/A")
								print(Fore.GREEN+Style.BRIGHT+"     Ship Hull Cost"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.costofshipshull}"+Fore.GREEN+Style.BRIGHT+"\t       Mine Max"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.minesmax}"+Fore.GREEN+Style.BRIGHT+"\t       Beacon Max"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.markerbeaconsmax}")
								print(Fore.GREEN+Style.BRIGHT+"     Ship Base Cost"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+str(shipbasecost)+Fore.GREEN+Style.BRIGHT+"\t    Genesis Max"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.genesistorpedoes}"+Fore.GREEN+Style.BRIGHT+"\t  Long Range Scan"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.cargoholdsstart}")
								print(Fore.GREEN+Style.BRIGHT+"Max Figs Per Attack"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.fighterattackforce}"+Fore.GREEN+Style.BRIGHT+"\tTranswarp Drive"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.transwarpdrive}"+Fore.GREEN+Style.BRIGHT+"\t   Planet Scanner"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.planetscanner}")
								print(Fore.GREEN+Style.BRIGHT+"      Maximum Holds"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.cargoholdsmax}"+Fore.GREEN+Style.BRIGHT+"\tTransport Range"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+f"{shipclass.cargoholdsmax}"+Fore.GREEN+Style.BRIGHT+"\t  Photon Missiles"+Fore.YELLOW+Style.BRIGHT+":   "+Fore.CYAN+Style.BRIGHT+ptlauncher)
							elif found == False:
								print("")
								print(Fore.GREEN+"The Vid Term doesn't recognize your choice. Try again.")

							# If not exists, print "I can't seem to find that ship reference."
		match command:
			case 'p': # Buy class 0 items
				pass
			case 'r': # Change ship registration
				pass
			case '?': # Display menu
				print("")
				print(Fore.GREEN+Style.BRIGHT+"  The Federation Shipards"+Fore.YELLOW+Style.BRIGHT+":")
				print("")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"B"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Buy a New Ship")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"S"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Sell Extra Ships")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"E"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Examine Ship Specs")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"P"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Buy Class 0 Items")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"R"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Change Ship Registration")
				print("")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.YELLOW+Style.BRIGHT+"!"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.YELLOW+Style.BRIGHT+"Shipyards Help")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.YELLOW+Style.BRIGHT+"Q"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.YELLOW+Style.BRIGHT+"Leave the Shipyards")
			case '!': # Shipyards help
				pass
			case 'q': # Leave the shipyards.
				print(Fore.GREEN+"You leave the shipyards.")
				break
			case _:
				print(Fore.GREEN+"You can't seem to find anyone to talk to.")

def playership(path,slash,player):
	command = ""
	while command != "q":
		print("")
		print (Fore.MAGENTA+Style.BRIGHT+"Command: ["+Fore.CYAN+Style.BRIGHT+f"{player.locationx}, {player.locationy}"+Fore.MAGENTA+Style.BRIGHT+"] ("+Fore.YELLOW+Style.BRIGHT+"?=Help"+Fore.MAGENTA+Style.BRIGHT+"): ")
		command = input("")
		match command:
			case "a": # Attack enemy ship
				pass
			case "b": # Interdictor control
				pass
			case "c": # Onboard Computer
				pass
			case "d": # Display the sector
				pass
			case "e": # Sub-space Etherprobe
				pass
			case "f": # Take or leave fighters
				pass
			case "g": # Show deployed fighters
				pass
			case "h": # Handle space mines
				pass
			case "i": # Ship information
				print(Fore.WHITE+Back.BLUE+Style.BRIGHT+"<Info>")
				print("")
				print(Fore.MAGENTA+Style.BRIGHT+"Trader Name    "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+player.rank+" "+player.firstname+" "+player.middlename+" "+player.lastname)
				print(Fore.MAGENTA+Style.BRIGHT+"Experience     "+Fore.YELLOW+Style.BRIGHT+": "+Fore.CYAN+Style.BRIGHT+player.xp+Fore.GREEN+Style.BRIGHT+" points")
				print(Fore.MAGENTA+Style.BRIGHT+"Kills          "+Fore.YELLOW+Style.BRIGHT+": "+Fore.CYAN+Style.BRIGHT+player.kills)
				print(Fore.MAGENTA+Style.BRIGHT+"Times Blown Up "+Fore.YELLOW+Style.BRIGHT+": "+Fore.CYAN+Style.BRIGHT+player.deaths)
				print(Fore.MAGENTA+Style.BRIGHT+"Ship Name      "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Ship Info      "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Date Built     "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Turns to Warp  "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Current Sector "+Fore.YELLOW+Style.BRIGHT+": "+Fore.CYAN+Style.BRIGHT+player.locationx+", "+player.locationy)
				print(Fore.MAGENTA+Style.BRIGHT+"Turns Left     "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Total Holds    "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Fighters       "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Shield Points  "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"LongRange Scan "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
				print(Fore.MAGENTA+Style.BRIGHT+"Credits        "+Fore.YELLOW+Style.BRIGHT+": "+Fore.GREEN+Style.BRIGHT+"")
			case "j": # Jettison cargo 
				pass
			case "l": # Land on a planet 
				pass
			case "m": # Move to a sector
				pass
			case "n": # Move to NavPoint
				pass
			case "o": # Starport construction
				pass
			case "p": # Dock with the station
				player.whereami = "station"
				p.playersave(path,slash,player.userid,player.firstname,player.middlename,player.lastname,player.alignment,player.rank,player.branch,player.xp,player.kills,player.deaths,player.locationx,player.locationy,player.whereami,player.health,player.species,player.age,player.birthday,player.homeplanet,player.languages)
				break
			case 'q': # Quit the whole game.
				print(Fore.WHITE+Back.BLUE+Style.BRIGHT+"Live long and prosper.")
				quit()
			case "r": # Release beacon
				pass	
			case "s": # Long range scan
				pass	
			case "t": # Corporate menu
				pass
			case "u": # Use genesis torpedo
				pass	
			case "v": # View game status
				pass	
			case "w": # Tow spavcecraft
				pass	
			case "x": # Transporter pad
				pass	
			case "y": # Set NavPoints
				pass
			case '?': # Help				
				print("")
				print(Fore.BLUE+Style.BRIGHT+"                             SHIP OPTIONS")
				print("")
				print(Fore.MAGENTA+Style.BRIGHT+"       Navigation              Computer              Tactical")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"D"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Re-Display Sector "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"C"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Onboard Computer "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"A"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Attack Enemy Ship")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"P"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Port and Trade    "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"X"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Transporter Pad  "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"E"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Sub-Space EtherProbe")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"M"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Move to a Sector  "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"I"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Ship Information "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"F"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Take or Leave Fighters")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"L"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Land on a Planet  "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"T"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Corporate Menu   "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"G"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Show Deployed Fighters")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"S"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Long Range Scan   "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"U"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Use Genesis Torp "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"H"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Handle Space Mines")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"R"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Release Beacon    "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"J"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Jettison Cargo   "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"K"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Show Deployed Mines")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"W"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Tow SpaceCraft    "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"B"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Interdict Ctrl   "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"O"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Starport Construction")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"N"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Move to NavPoint  "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.YELLOW+Style.BRIGHT+"!"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.YELLOW+Style.BRIGHT+"Stardock Help    "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.GREEN+Style.BRIGHT+"Y"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.CYAN+Style.BRIGHT+"Set NavPoints")
				print(Fore.MAGENTA+Style.BRIGHT+" <"+Fore.RED+Style.BRIGHT+"Q"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.RED+Style.BRIGHT+"Quit the Game     "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.YELLOW+Style.BRIGHT+"Z"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.YELLOW+Style.BRIGHT+"Star Trek Docs   "+Fore.MAGENTA+Style.BRIGHT+" <"+Fore.YELLOW+Style.BRIGHT+"V"+Fore.MAGENTA+Style.BRIGHT+"> "+Fore.YELLOW+Style.BRIGHT+"View Game Status")
			case _: # Display the sector.
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
'''