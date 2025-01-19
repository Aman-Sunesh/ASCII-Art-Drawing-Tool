import curses    # pip install windows-curses
import os

# Function to save the grid to a file
def save_to_file(grid, filename="ascii_art.txt"):
    with open(filename, "w") as file:
        for row in grid:
            file.write("".join(row) + "\n")

    curses.endwin()
    print(f"Art saved to {filename}")


# Function to resize the grid
def resize_grid(grid, new_height, new_width):
    current_height = len(grid)
    current_width = len(grid[0]) if current_height > 0 else 0

    # Crop or expand rows
    grid = grid[:new_height] + [[" " for _ in range(current_width)] for _ in range(new_height - len(grid))]

    # Adjust columns in each row
    for i in range(len(grid)):
        grid[i] = grid[i][:new_width] + [" " for _ in range(new_width - len(grid[i]))]

    return grid


# Main drawing tool function
def ascii_art_tool(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.keypad(True)  # Enable special keys like arrows

    # Get terminal size
    term_height, term_width = curses.LINES, curses.COLS

    # Initial grid dimensions (must fit within the terminal)
    height, width = min(20, term_height - 3), min(40, term_width - 1)
    grid = [[" " for _ in range(width)] for _ in range(height)]

    # Cursor position
    cursor_y, cursor_x = 0, 0

    undo_stack = []

    while True:
        # Check terminal size dynamically
        term_height, term_width = curses.LINES, curses.COLS

        if height > term_height - 3 or width > term_width - 1:
            stdscr.clear()
            stdscr.addstr(0, 0, "Terminal too small for the current grid. Resize your terminal and restart.")
            stdscr.refresh()
            stdscr.getch()
            break

        # Display grid
        stdscr.clear()
        
        for y, row in enumerate(grid):
            if y < term_height - 3:
                stdscr.addstr(y, 0, "".join(row[:term_width - 1]))

        # Display instructions
        stdscr.addstr(height + 1, 0, "[Arrows] Move  [Char] Draw  [Space] Erase  [Ctrl+S] Save  [U] Undo  [R] Resize  [Q] Quit")
        stdscr.addstr(height + 2, 0, f"Cursor: ({cursor_y + 1}, {cursor_x + 1})")
        stdscr.refresh()

        # Handle user input
        key = stdscr.getch()

        if key == curses.KEY_UP and cursor_y > 0:
            cursor_y -= 1
        elif key == curses.KEY_DOWN and cursor_y < height - 1:
            cursor_y += 1
        elif key == curses.KEY_LEFT and cursor_x > 0:
            cursor_x -= 1
        elif key == curses.KEY_RIGHT and cursor_x < width - 1:
            cursor_x += 1
        elif key == ord("q"):
            break
        elif key == ord(" "):
            undo_stack.append([row[:] for row in grid])
            grid[cursor_y][cursor_x] = " "
        elif key == 19:  # Ctrl+S (Save)
            save_to_file(grid)
        elif key == ord("u") and undo_stack:
            grid = undo_stack.pop()
        elif key == ord("r"):
            stdscr.addstr(height + 3, 0, "Enter new dimensions (height width): ")
            stdscr.refresh()
            curses.echo()

            try:
                new_dims = stdscr.getstr(height + 3, 32).decode("utf-8").split()
                new_height, new_width = int(new_dims[0]), int(new_dims[1])
                undo_stack.append([row[:] for row in grid])
                grid = resize_grid(grid, min(new_height, term_height - 3), min(new_width, term_width - 1))
                height, width = min(new_height, term_height - 3), min(new_width, term_width - 1)

            except:
                stdscr.addstr(height + 4, 0, "Invalid dimensions. Press any key to continue.")
                stdscr.getch()
            curses.noecho()

        elif 32 <= key <= 126:  # Printable characters
            undo_stack.append([row[:] for row in grid])
            grid[cursor_y][cursor_x] = chr(key)


# Run the ASCII Art Tool if executed directly
if __name__ == "__main__":
    curses.wrapper(ascii_art_tool)
