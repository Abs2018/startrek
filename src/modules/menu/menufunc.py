from modules import art


def title(title):
    left_spaces, right_spaces = art.title_center(title, 80)
    print("")
    art.cd(226, '', left_spaces+title.upper()+right_spaces, "reset", True)
    print("")


def option(option, text):
    # Print the Option
    art.cd(5, '', "<", "", False)
    art.cd(2, '', str(option.upper()), "", False)
    art.cd(5, '', "> ", "", False)
    # Print the text
    art.cd("light_cyan", '', text.title()+"\t\t", "reset", True)


def prompt(text):
    print("")
    art.cd('light_cyan', '', str(text)+" ", 'reset', False)
    art.cd('226', '', "[?]", 'reset', False)
    art.cd('light_cyan', '', ": ", 'reset', False)


def error(message="Invalid Choice. Please Try Again."):
    print("")
    art.cd("red", "", message, "reset", True)
    choice = input()


def quit(text):
    print("")
    art.cd(5, '', "<", "", False)
    art.cd('226', '', "Q", "", False)
    art.cd(5, '', "> ", "", False)
    art.cd(100, '', str(text), "", True)
    # Footer
    art.cd("", "", "", "reset", True)
