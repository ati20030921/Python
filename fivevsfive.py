from tkinter import *
import random

BOARD_SIZE = 8
WIN_LENGTH = 4

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        result = check_winner()
        if result is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn")
        elif result is True:
            label.config(text=player + " wins!")
        elif result == "Tie":
            label.config(text="Tie!")

def check_winner():
    def check_direction(r, c, dr, dc):
        symbol = buttons[r][c]['text']
        if symbol == "":
            return False
        for i in range(1, WIN_LENGTH):
            nr, nc = r + dr*i, c + dc*i
            if not (0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE):
                return False
            if buttons[nr][nc]['text'] != symbol:
                return False
        for i in range(WIN_LENGTH):
            buttons[r + dr*i][c + dc*i].config(bg="lightblue")
        return True

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if (check_direction(r, c, 0, 1) or   # vízszintes
                check_direction(r, c, 1, 0) or   # függőleges
                check_direction(r, c, 1, 1) or   # átló \
                check_direction(r, c, 1, -1)):   # átló /
                return True

    if all(buttons[r][c]['text'] != "" for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)):
        return "Tie"

    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            buttons[r][c].config(text="", bg="#4d4dff")

# GUI setup
window = Tk()
window.title("Tic-Tac-Toe 8x8")

players = ["X", "O"]
player = random.choice(players)

label = Label(text=player + " turn", font=('consolas', 20))
label.pack(side="top")

reset_button = Button(text="New Game", font=('consolas', 16), command=new_game)
reset_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

for r in range(BOARD_SIZE):
    for c in range(BOARD_SIZE):
        buttons[r][c] = Button(frame, text="", font=('consolas', 20), width=3, height=1,
                               command=lambda r = r, c=c: next_turn(r, c))
        buttons[r][c].grid(row=r, column=c)

window.mainloop()
