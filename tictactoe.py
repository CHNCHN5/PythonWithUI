import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, Bruh):
        self.Eyow = Bruh
        self.Eyow.title("Tic Tac Toe")
        self.Eyow.configure(bg='#00FFC9')

        self.title_label = tk.Label(self.Eyow, text="Tic Tac Toe", font=('bold', 16), bg='#00FFC9')
        self.title_label.grid(row=0, column=1, pady=10)

        self.current_player = "X"
        self.board = [" "]*9

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.Eyow, text=" ", font=('normal', 20), width=6, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col),
                                   bg='#00DAAC', fg='#000000')
                button.grid(row=i + 1, column=j, padx=1, pady=2)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tapos ang laban", f"Player {self.current_player} ang Panalo!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tapos ang laban", "Patas lang!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self):

        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != " ":
                return True
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ")
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
