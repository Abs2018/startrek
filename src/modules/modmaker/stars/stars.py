from modules import art
from modules.menu import menufunc
from modules.modmaker.stars import view
from modules.modmaker.stars import create
from modules.modmaker.stars import edit


def menu():
    while True:
        art.clear()
        menufunc.title("Star Classes")
        menufunc.option("V", "View Star Class")
        menufunc.option("C", "Create Star Class")
        menufunc.option("E", "Edit Star Class")
        menufunc.option("D", "Delete Star Class")
        menufunc.quit("Back to ModMaker")
        menufunc.prompt("Enter your choice")
        choice = input("")

        if choice.lower() == "v":
            # Provide list of Star Classes
            view.view_star_classes()
        elif choice.lower() == "c":
            create.create_star_class()
        elif choice.lower() == "e":
            edit.edit_star_class()
        elif choice.lower() == "d":
            break
        elif choice.lower() == "q":
            break
        elif choice == "?":
            pass
        else:
            menufunc.error()
