import curses

def draw_canvas(stdscr, canvas, colors):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    # Draw top and bottom borders
    for x in range(width - 1):
        stdscr.addstr(0, x, "-", curses.color_pair(colors.index("white") + 1))
        stdscr.addstr(height - 1, x, "-", curses.color_pair(colors.index("white") + 1))
    
    # Draw left and right borders
    for y in range(1, height - 1):
        stdscr.addstr(y, 0, "|", curses.color_pair(colors.index("white") + 1))
        stdscr.addstr(y, width - 2, "|", curses.color_pair(colors.index("white") + 1))
    
    for y, row in enumerate(canvas):
        for x, (char, color) in enumerate(row):
            if y < height - 1 and x * 2 < width - 2:
                if char.strip():  # Check if the character is not empty
                    stdscr.addstr(y, x * 2, char, curses.color_pair(colors.index(color) + 1))
                else:
                    stdscr.addstr(y, x * 2, char)  # Use default color pair for empty characters
    stdscr.refresh()


def display_char_prompt(stdscr, colors):
    stdscr.clear()
    stdscr.addstr(0, 0, "Select a character:", curses.A_BOLD)
    char_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-=_+[]{}|;:',.<>/?`~\\\""
    for i, char in enumerate(char_list):
        stdscr.addstr(i // 16 + 2, (i % 16) * 2, char)
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == 27:  # Escape key
            return None
        elif chr(key) in char_list:
            return chr(key)

def display_color_prompt(stdscr, colors):
    stdscr.clear()
    stdscr.addstr(0, 0, "Select a color:", curses.A_BOLD)
    for i, color in enumerate(colors):
        stdscr.addstr(i + 2, 0, f"{i + 1}: {color}")
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == 27:  # Escape key
            return None
        elif key >= ord('1') and key <= ord('0') + len(colors):
            return colors[key - ord('1')]

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)

    canvas = [["  " for _ in range(40)] for _ in range(20)]  # Initialize a 40x20 canvas
    colors = ["white", "red", "green", "blue"]
    color_idx = 0
    y, x = 1, 1  # Initial cursor position (inside the border)
    char = "  "  # Initial character

    while True:
        draw_canvas(stdscr, canvas, colors)
        stdscr.addstr(y, x * 2, char, curses.color_pair(colors.index(colors[color_idx]) + 1))
        key = stdscr.getch()

        if key == curses.KEY_UP:
            y = max(1, y - 1)
        elif key == curses.KEY_DOWN:
            y = min(len(canvas) - 2, y + 1)
        elif key == curses.KEY_LEFT:
            x = max(1, x - 1)
        elif key == curses.KEY_RIGHT:
            x = min(len(canvas[0]) // 2 - 2, x + 1)
        elif key == ord('g'):
            selected_char = display_char_prompt(stdscr, colors)
            if selected_char:
                char = selected_char
        elif key == ord('c'):
            selected_color = display_color_prompt(stdscr, colors)
            if selected_color:
                color_idx = colors.index(selected_color)
        elif key == ord('q'):
            break

        canvas[y][x] = (char, colors[color_idx])

curses.wrapper(main)
