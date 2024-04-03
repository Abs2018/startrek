from modules import art
from modules.menu import menufunc
from modules.modmaker.stars import stars

# 72×23

# Create the main menu
def menu():
    while True:
        art.clear()
        menufunc.title("Star Trek Modmaker")
        menufunc.option("s", "stars classes")
        menufunc.option("p", "planet classes")
        menufunc.option("e", "empires")
        menufunc.option('r', 'races')
        menufunc.option("v", "ship classes")
        menufunc.quit("Quit ModMaker")
        menufunc.prompt("Enter your choice")
        choice = input("")

        if choice.lower() == "e":
            pass
        elif choice.lower() == "p":
            pass
        elif choice.lower() == "s":
            stars.menu()
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice.lower() == "q":
            print("")
            art.cd(0, 196, "  Live long and prosper  ", 'reset', True)
            print("")
            quit()
        elif choice == "?":
            pass
        else:
            menufunc.error()


# Run the main menu.
menu()
