# ASCII Art Tool

## Overview
The **ASCII Art Tool** is a terminal-based application that allows users to create and edit ASCII art in an interactive grid. Users can draw characters, erase, resize the grid, save their work to a file, and undo changes. It leverages Python's `curses` library for interactive terminal control.

## Prerequisites
Before running the ASCII Art Tool, ensure you have the following:

- **Python 3.6 or higher**
- **curses library** (pre-installed on most Unix-based systems)
- On **Windows**, install `windows-curses`:
  ```bash
  pip install windows-curses
  ```

## Installation

### 1. Clone the Repository
Clone the ASCII Art Tool repository from GitHub:

  ```bash
  git clone https://github.com/yourusername/ASCII-Art-Drawing-Tool.git
  cd ASCII-Art-Drawing-Tool
  ```

### 2. Run the Application
Run the application directly using:

  ```bash
  python3 ASCII_Art_Drawing_Tool.py
  ```

## Features and Functionalities

### Interactive Grid
- A resizable grid for creating ASCII art.
- Real-time cursor movement using arrow keys.
- Ability to draw, erase, and undo edits.

### Save Art to File
- Save the current grid to a `.txt` file using the `Ctrl+S` command.

### Undo and Redo
- Undo the last action with the `U` key.

### Grid Resizing
- Resize the grid dynamically using the `R` key.

### User-Friendly Controls
- Intuitive keyboard controls for navigation and editing.

---

## Usage

### Controls
- **Arrow Keys**: Move the cursor.
- **[Char]**: Draw a character at the current cursor position.
- **Space**: Erase the character at the current cursor position.
- **Ctrl+S**: Save the current grid to a file (`ascii_art.txt`).
- **U**: Undo the last change.
- **R**: Resize the grid by specifying new dimensions.
- **Q**: Quit the application.

### Instructions

#### Draw ASCII Art:
1. Move the cursor to the desired position using the arrow keys.
2. Enter a character to draw it at the cursor's location.
3. Use the spacebar to erase characters.

#### Undo:
- Press `U` to undo the most recent action.

#### Resize the Grid:
1. Press `R` and enter new dimensions (height and width).
2. Ensure the dimensions fit within your terminal's size.

#### Save Your Work:
1. Press `Ctrl+S` to save the grid to `ascii_art.txt`.
2. The file will be saved in the current working directory.

#### Quit:
- Press `Q` to exit the application.

---

## Sample Output

Here is a screenshot showcasing a sample ASCII art created using the tool. It highlights the interactive grid and the drawn characters.

![Sample Output](Output%20Image.png)

---

## Troubleshooting

### 1. Terminal Too Small
- If the terminal is too small for the current grid, resize your terminal window and restart the application.

### 2. Invalid Dimensions
- Ensure you input valid numeric values when resizing the grid.

### 3. File Not Saved
- Verify you have write permissions in the current directory.

### 4. Windows-Specific Issues
- Ensure `windows-curses` is installed if you're running the application on Windows.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or additional features. Whether it's enhancing the algorithm, optimizing performance, or adding new functionalities, your contributions are valuable.

---

## Acknowledgments
- **Python Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **curses Library Documentation**: [https://docs.python.org/3/library/curses.html](https://docs.python.org/3/library/curses.html)
- **Open Source Community**: For tools and resources.


