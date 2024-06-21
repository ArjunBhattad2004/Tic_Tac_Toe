import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.sign_player1 = None
        self.sign_player2 = None

        self.create_start_screen()

    def create_start_screen(self):
        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack()

        tk.Label(self.start_frame, text="Player 1 Name:").grid(row=0, column=0)
        self.player1_entry = tk.Entry(self.start_frame)
        self.player1_entry.grid(row=0, column=1)

        tk.Label(self.start_frame, text="Player 2 Name:").grid(row=1, column=0)
        self.player2_entry = tk.Entry(self.start_frame)
        self.player2_entry.grid(row=1, column=1)

        tk.Label(self.start_frame, text="Player 1 Sign (X or O):").grid(row=2, column=0)
        self.sign_player1_entry = tk.Entry(self.start_frame)
        self.sign_player1_entry.grid(row=2, column=1)

        tk.Label(self.start_frame, text="Player 2 Sign (X or O):").grid(row=3, column=0)
        self.sign_player2_entry = tk.Entry(self.start_frame)
        self.sign_player2_entry.grid(row=3, column=1)

        start_button = tk.Button(self.start_frame, text="Start Game", command=self.start_game)
        start_button.grid(row=4, columnspan=2)

    def start_game(self):
        player1_name = self.player1_entry.get()
        player2_name = self.player2_entry.get()
        self.sign_player1 = self.sign_player1_entry.get()
        self.sign_player2 = self.sign_player2_entry.get()

        if player1_name and player2_name and self.sign_player1 and self.sign_player2:
            if self.sign_player1.upper() not in ["X", "O"] or self.sign_player2.upper() not in ["X", "O"]:
                messagebox.showerror("Error", "Invalid signs! Please choose X or O.")
                return
            elif self.sign_player1.upper() == self.sign_player2.upper():
                messagebox.showerror("Error", "Signs should be different for both players!")
                return

            self.player1 = (player1_name, self.sign_player1.upper())
            self.player2 = (player2_name, self.sign_player2.upper())
            self.current_player = self.player1
            self.create_game_screen()
            self.start_frame.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    def create_game_screen(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.buttons = [[None, None, None] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.game_frame, text="", font=("Helvetica", 20), width=5, height=2,
                                                    command=lambda row=row, col=col: self.on_click(row, col))
                self.buttons[row][col].grid(row=row, column=col, sticky="nsew")

        self.reset_button = tk.Button(self.game_frame, text="Reset", font=("Helvetica", 14), command=self.reset_game)
        self.reset_button.grid(row=3, column=1, columnspan=3, sticky="ew")

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""
        self.current_player = self.player1

    def check_win(self):
        # Rows
        for row in range(3):
            if self.buttons[row][0]["text"] == self.buttons[row][1]["text"] == self.buttons[row][2]["text"] != "":
                return True

        # Columns
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != "":
                return True

        # Diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player[1]
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player[0]} wins!")
                self.reset_game()
            elif all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3)):
                messagebox.showinfo("Tic Tac Toe", "Game Draws")
                self.reset_game()
            else:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
