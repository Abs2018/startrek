command = ""
while command != "q":
    if command == "":
        command = input("Press any key: ")

    match command:
        case ('q' | 'Q'):
            quit()
        case _:
            print("Your key press was: "+str(command))
            command = ""
