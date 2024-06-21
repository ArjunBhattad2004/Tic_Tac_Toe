# **Tic Tac Toe Game**
This project is a simple implementation of the classic Tic Tac Toe game using two different graphical user interfaces: Tkinter and PyQt. The game supports two-player mode, where players can input their names and choose their symbols before starting the game.

## Features
-Two-player mode with customizable player names and symbols.

-GUI implemented using Tkinter and PyQt.

-Option to reset/restart the game.

-Displays the winner or if the game is a draw.

-Highlights the current player's turn.

## Requirements
-Python 3.x

-Tkinter (comes pre-installed with Python)

-PyQt5

## Installation
For Tkinter version:
Tkinter is included with Python, so no additional installation is required.

For PyQt version:

Install PyQt5 using pip:

<code>pip install PyQt5 </code>


## Code Overview
### Tkinter Version
#### TicTacToeGame class: This class handles the game logic and GUI for the Tkinter version.

__init__: Initializes the game and creates the start screen.

create_start_screen: Creates the screen for players to input their names and symbols.

start_game: Validates the inputs and starts the game if inputs are valid.

create_game_screen: Creates the game board.

reset_game: Resets the game board.

check_win: Checks if a player has won.

on_click: Handles the button click events on the game board.

### PyQt Version

#### StartGameWindow class: This class handles the initial screen where players input their names and symbols.

__init__: Initializes the start screen.

apply_colorful_theme: Applies a colorful theme to the GUI.

start_game: Starts the game by opening the TicTacToeWindow with the provided inputs.

#### TicTacToeWindow class: This class handles the game logic and GUI for the PyQt version.

__init__: Initializes the game board and displays the player names and symbols.

on_button_click: Handles button click events on the game board.

check_winner: Checks if a player has won or if the game is a draw.

show_winner: Displays the winner and disables the buttons.

show_draw: Displays a draw message and disables the buttons.

disable_buttons: Disables all buttons on the game board.

enable_buttons: Enables all buttons and clears the board.

restart_game: Resets the game board and starts a new game.

update_turn_label: Updates the label to show the current player's turn.

## Usage
### Starting the Game:

Input Player 1 and Player 2 names.

Choose symbols (X or O) for Player 1 (Player 2 will automatically get the other symbol).

Click "Start Game".

### Playing the Game:

Players take turns clicking on the game board.

The current player's symbol is displayed on the clicked cell.

The game checks for a winner or a draw after each move.

### Resetting/Restarting the Game:

Use the "Reset" button in the Tkinter version or "Restart Game" button in the PyQt version to start a new game.

## Screenshots
### Tkinter Version

![image](https://github.com/ArjunBhattad2004/Tic_Tac_Toe/assets/163147180/0a706cea-a01a-4b78-a8ea-c254838049fc)

![image](https://github.com/ArjunBhattad2004/Tic_Tac_Toe/assets/163147180/812d78e8-7446-4e9a-9ea3-11d4e7cb35cd)




### PyQt Version

![image](https://github.com/ArjunBhattad2004/Tic_Tac_Toe/assets/163147180/ab1e6f0e-fd0e-482b-bd72-04d01d254685)

![image](https://github.com/ArjunBhattad2004/Tic_Tac_Toe/assets/163147180/4d55babc-b25d-4404-bd26-d4afa2ced5fb)


