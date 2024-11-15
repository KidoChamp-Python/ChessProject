import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Chess Board Game")

button_chess_notation = {}

# Load images
cream = Image.open("D:\\Downloads\\#ffffcc100x100.png")
cream = ImageTk.PhotoImage(cream)
green = Image.open("D:\\Downloads\\#669933 100x100.png")
green = ImageTk.PhotoImage(green)

pixel = tk.PhotoImage(width=1, height=1)

# Chess pieces setup (example)
white_pieces = [(8, 1), (7, 2), (6, 3), (5, 4), (4, 5)]  # Example positions of white pieces

rook_position = 7, 2  # Current position of the rook
new_rook_position = 1, 1 # Target position
moves_to_check = []

# Logic for rook's movement
if rook_position[0] == new_rook_position[0]:  # Same row
    x = rook_position[1] - new_rook_position[1]
    if x < 0:  # Moving right
        for number in range(1, -x + 1):
            moves_to_check.append([rook_position[0], rook_position[1] + number])
            if moves_to_check[number - 1] in white_pieces:
                break
    elif x > 0:  # Moving left
        for number in range(1, x + 1):
            moves_to_check.append([rook_position[0], rook_position[1] - number])
            if moves_to_check[number - 1] in white_pieces:
                break
elif rook_position[1] == new_rook_position[1]:  # Same column
    x = rook_position[0] - new_rook_position[0]
    if x < 0:  # Moving down
        for number in range(1, -x + 1):
            moves_to_check.append([rook_position[0] + number, rook_position[1]])
            if moves_to_check[number - 1] in white_pieces:
                break
    elif x > 0:  # Moving up
        for number in range(1, x + 1):
            moves_to_check.append([rook_position[0] - number, rook_position[1]])
            if moves_to_check[number - 1] in white_pieces:
                break

if tuple(new_rook_position) in [tuple(move) for move in moves_to_check]:
    print("Move is legal!")



print(moves_to_check)

