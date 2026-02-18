import tkinter as tk
from tkinter import messagebox

# Game variables
current_player = "X"
board = [""] * 9

# Check winner
def check_winner():
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != "":
            return True
    return False

# Check draw
def check_draw():
    return "" not in board

# Button click
def click(btn, index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        btn.config(text=current_player)

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} Wins!")
            reset_game()
            return
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"
        label.config(text=f"Player {current_player}'s Turn")

# Reset game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    label.config(text="Player X's Turn")
    for btn in buttons:
        btn.config(text="")

# GUI window
root = tk.Tk()
root.title("Tic Tac Toe - 2 Player Touch Game")
root.geometry("300x350")

label = tk.Label(root, text="Player X's Turn", font=("Arial", 16))
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda i=i: click(buttons[i], i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Restart Game", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()

