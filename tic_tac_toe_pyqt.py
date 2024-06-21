import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QLineEdit, QComboBox
from PyQt5.QtCore import Qt

# Global variables
board = [['' for _ in range(3)] for _ in range(3)]
turn = 'X'

class StartGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe - Start Game")
        self.setGeometry(100, 100, 400, 250)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QGridLayout(centralWidget)

        self.player1_label = QLabel("Player 1 Name:", self)
        layout.addWidget(self.player1_label, 0, 0)
        self.player1_edit = QLineEdit(self)
        layout.addWidget(self.player1_edit, 0, 1)

        self.player2_label = QLabel("Player 2 Name:", self)
        layout.addWidget(self.player2_label, 1, 0)
        self.player2_edit = QLineEdit(self)
        layout.addWidget(self.player2_edit, 1, 1)

        self.symbol_label = QLabel("Choose Symbol for Player 1:", self)
        layout.addWidget(self.symbol_label, 2, 0)
        self.symbol_combo = QComboBox(self)
        self.symbol_combo.addItems(['X', 'O'])
        layout.addWidget(self.symbol_combo, 2, 1)

        self.note_label = QLabel("Note: X goes first", self)
        layout.addWidget(self.note_label, 3, 0, 1, 2)
        self.note_label.setAlignment(Qt.AlignCenter)

        self.start_button = QPushButton("Start Game", self)
        self.start_button.clicked.connect(self.start_game)
        layout.addWidget(self.start_button, 4, 0, 1, 2)

        # Apply colorful theme
        self.apply_colorful_theme()

    def apply_colorful_theme(self):
        # Background color
        self.setStyleSheet("background-color: #f2f2f2;")

        # Button color
        button_stylesheet = """
            QPushButton {
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker Green */
            }
        """
        self.start_button.setStyleSheet(button_stylesheet)

        # Label color
        label_stylesheet = """
            QLabel {
                color: #333;
                font-size: 16px;
            }
        """
        self.player1_label.setStyleSheet(label_stylesheet)
        self.player2_label.setStyleSheet(label_stylesheet)
        self.symbol_label.setStyleSheet(label_stylesheet)
        self.note_label.setStyleSheet(label_stylesheet)

    def start_game(self):
        global turn
        player1_name = self.player1_edit.text()
        player2_name = self.player2_edit.text()
        player1_symbol = self.symbol_combo.currentText()
        player2_symbol = 'O' if player1_symbol == 'X' else 'X'

        game_window = TicTacToeWindow(player1_name, player2_name, player1_symbol, player2_symbol)
        game_window.show()
        self.close()

class TicTacToeWindow(QMainWindow):
    def __init__(self, player1_name, player2_name, player1_symbol, player2_symbol):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 400, 450)  # Increased height to accommodate the restart button

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        layout = QGridLayout(centralWidget)
        layout.setSpacing(0)

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = QPushButton('', self)
                button.setFixedSize(120, 120)
                button.clicked.connect(lambda _, row=i, col=j: self.on_button_click(row, col))
                button.setStyleSheet("font-size: 36px;")  # Increase font size
                row_buttons.append(button)
                layout.addWidget(button, i, j)
            self.buttons.append(row_buttons)

        self.restart_button = QPushButton("Restart Game", self)
        self.restart_button.clicked.connect(self.restart_game)
        layout.addWidget(self.restart_button, 3, 0, 1, 3)

        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label, 4, 0, 1, 3)  # Moved the result label to row 4
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 20px;")  # Increase font size for result label

        self.turn_label = QLabel("", self)
        layout.addWidget(self.turn_label, 5, 0, 1, 3)  # Added label for current player's turn
        self.turn_label.setAlignment(Qt.AlignCenter)
        self.turn_label.setStyleSheet("font-size: 16px;")  # Increase font size for turn label

        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_symbol = player1_symbol
        self.player2_symbol = player2_symbol
        self.current_player = player1_name

        self.update_turn_label()

    def on_button_click(self, row, col):
        global turn
        button = self.buttons[row][col]
        if button.text() == '':
            button.setText(turn)
            board[row][col] = turn
            self.check_winner()
            turn = self.player2_symbol if turn == self.player1_symbol else self.player1_symbol
            self.update_turn_label()

    def check_winner(self):
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != '':
                self.show_winner(row[0])
                return

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != '':
                self.show_winner(board[0][col])
                return

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != '':
            self.show_winner(board[0][0])
            return
        if board[0][2] == board[1][1] == board[2][0] != '':
            self.show_winner(board[0][2])
            return

        # Check for draw
        if all(cell != '' for row in board for cell in row):
            self.show_draw()

    def show_winner(self, winner_symbol):
        winner_name = self.player1_name if winner_symbol == self.player1_symbol else self.player2_name
        self.result_label.setText(f"{winner_name} wins!")
        self.result_label.setStyleSheet("font-size: 24px;")  # Increase font size for winner message
        self.disable_buttons()

    def show_draw(self):
        self.result_label.setText("Game Draw!")
        self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def enable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(True)
                button.setText('')

    def restart_game(self):
        global board, turn
        board = [['' for _ in range(3)] for _ in range(3)]
        turn = 'X'
        self.result_label.clear()
        self.enable_buttons()
        self.current_player = self.player1_name
        self.update_turn_label()

    def update_turn_label(self):
        self.turn_label.setText(f"{self.current_player}'s turn")
        self.current_player = self.player2_name if self.current_player == self.player1_name else self.player1_name

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = StartGameWindow()
    start_window.show()
    sys.exit(app.exec_())




