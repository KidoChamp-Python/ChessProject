import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Chess Board Game")

button_chess_notation= {}


#Before Code:

#Button Color As Image (Makes buttons without pieces clickable)
cream = Image.open("D:\Downloads\#ffffcc100x100.png")
cream = ImageTk.PhotoImage(cream)
green = Image.open("D:\Downloads\#669933 100x100.png")
green = ImageTk.PhotoImage(green)

pixel= tk.PhotoImage(width=1,height=1)


white_knight = Image.open("D:\Downloads\WhiteKnight-1000x1000.png")  # Replace with your image path
white_knight = white_knight.resize((white_knight.width // 10, white_knight.height // 10))
white_knight = ImageTk.PhotoImage(white_knight)

black_knight = Image.open("D:\Downloads\Black Knight-1000x1000.png")  # Replace with your image path
black_knight = black_knight.resize((black_knight.width // 10, black_knight.height // 10))
black_knight = ImageTk.PhotoImage(black_knight)


white_rook = Image.open("D:\Downloads\White Rook-1000x1000.png")  # Replace with your image path
white_rook = white_rook.resize((white_rook.width // 10, white_rook.height // 10))
white_rook = ImageTk.PhotoImage(white_rook)


black_rook = Image.open("D:\Downloads\Black Rook-1000x1000.png")  # Replace with your image path
black_rook = black_rook.resize((black_rook.width // 10, black_rook.height // 10))
black_rook = ImageTk.PhotoImage(black_rook)


white_bishop = Image.open("D:\Downloads\LightBishop-1000x1000.png")  # Replace with your image path
white_bishop = white_bishop.resize((white_bishop.width // 10, white_bishop.height // 10))
white_bishop = ImageTk.PhotoImage(white_bishop)


black_bishop = Image.open("D:\Downloads\DarkBishop-1000x1000.png")  # Replace with your image path
black_bishop = black_bishop.resize((black_bishop.width // 10, black_bishop.height // 10))
black_bishop = ImageTk.PhotoImage(black_bishop)


white_king_a = Image.open("D:\Downloads\LightKing-1000x1000.png")  # Replace with your image path
white_king_a = white_king_a.resize((white_king_a.width // 10, white_king_a.height // 10))
white_king_a = ImageTk.PhotoImage(white_king_a)


black_king_a = Image.open("D:\Downloads\DarkKing-1000x1000.png")  # Replace with your image path
black_king_a = black_king_a.resize((black_king_a.width // 10, black_king_a.height // 10))
black_king_a = ImageTk.PhotoImage(black_king_a)

white_queen_image = Image.open("D:\Downloads\LightQueen-1000x1000.png")  # Replace with your image path
white_queen_image = white_queen_image.resize((white_queen_image.width // 10, white_queen_image.height // 10))
white_queen_image = ImageTk.PhotoImage(white_queen_image)


black_queen_image = Image.open("D:\Downloads\DarkQueen-1000x1000.png")  # Replace with your image path
black_queen_image = black_queen_image.resize((black_queen_image.width // 10, black_queen_image.height // 10))
black_queen_image = ImageTk.PhotoImage(black_queen_image)

white_pawn = Image.open("D:\Downloads\LightPawn-1000x1000.png")  # Replace with your image path
white_pawn = white_pawn.resize((white_pawn.width // 10, white_pawn.height // 10))
white_pawn = ImageTk.PhotoImage(white_pawn)


black_pawn = Image.open("D:\Downloads\DarkPawn-1000x1000.png")  # Replace with your image path
black_pawn = black_pawn.resize((black_pawn.width // 10, black_pawn.height // 10))
black_pawn = ImageTk.PhotoImage(black_pawn)





white_queen_rook = 8,1
white_queen_knight = 7,1
white_queen_bishop = 6,1
white_queen_a = 5,1
white_king = 4,1
white_king_bishop = 3,1
white_king_knight = 2,1
white_king_rook = 1,1

#White_Pawns
white_pawn1 = 1, 2
white_pawn2 = 2, 2
white_pawn3 = 3, 2
white_pawn4 = 4, 2
white_pawn5 = 5, 2
white_pawn6 = 6, 2
white_pawn7 = 7, 2
white_pawn8 = 8, 2


#Black_Pawns
black_pawn1 = 7,1
black_pawn2 = 7,2
black_pawn3 = 7,3
black_pawn4 = 7,4
black_pawn5 = 7,5
black_pawn6 = 7,6
black_pawn7 = 7,7
black_pawn8 = 7,8

button_numbers_with_pieces_at_start = [1, 6, 62, 57, 0, 7, 56, 63, 2, 5, 61, 58, 3, 59, 4, 60,8,9,10,11,12,13,14,15,48,49,50,51,52,53,54,55]

piece_to_move = None

root.geometry("900x900")

buttons= []
a=0
to_move = "white"
temperary_hold = 0
moves_to_check_wkr = []
moves_to_check_wkb = []
#Code: -=-=-=-=-=-=

def button_click(i):

    print(button_chess_notation[i])

    print(i)
    #Global:
    global moves_to_check_wkr
    global white_queen_rook
    global white_queen_knight
    global white_queen_bishop
    global white_queen_a
    global white_king
    global white_king_bishop
    global white_king_knight
    global white_king_rook

    # White_Pawns
    global white_pawn1
    global white_pawn2
    global white_pawn3
    global white_pawn4
    global white_pawn5
    global white_pawn6
    global white_pawn7
    global white_pawn8


    global a
    global temperary_hold
    global piece_to_move
    global to_move
    #White Pieces:o
    if a % 2 == 0:

        if button_chess_notation[i] == white_queen_rook:
            print(white_queen_rook)
        elif button_chess_notation[i] == white_queen_knight:
            print(white_queen_knight)
        elif button_chess_notation[i] == white_queen_bishop:
            print(white_queen_bishop)
        elif button_chess_notation[i] == white_queen_a:
            print(white_queen_a)
        elif button_chess_notation[i] == white_king:
            print(white_king)
        elif button_chess_notation[i] == white_king_bishop:
            print(white_king_bishop)
            a=a+1
            temperary_hold = i,"wkb"
        elif button_chess_notation[i] == white_king_knight:
            print(white_king_knight)
            a = a+1
            temperary_hold = i,"wkn"
        elif button_chess_notation[i] == white_king_rook:
            print(white_king_rook)
            a = a+1
            temperary_hold= i,"wkr"
            print(temperary_hold)
        elif button_chess_notation[i] == white_pawn1:
            print(white_pawn1)
        elif button_chess_notation[i] == white_pawn2:
            print(white_pawn2)
        elif button_chess_notation[i] == white_pawn3:
            print(white_pawn3)
        elif button_chess_notation[i] == white_pawn4:
            print(white_pawn4)
        elif button_chess_notation[i] == white_pawn5:
            print(white_pawn5)
        elif button_chess_notation[i] == white_pawn6:
            print(white_pawn6)
        elif button_chess_notation[i] == white_pawn7:
            print(white_pawn7)
        elif button_chess_notation[i] == white_pawn8:
            print(white_pawn8)
    else:
        if temperary_hold[1] == "wkn":

            if button_chess_notation[i] not in (
            white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7, white_pawn8,
            white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
            white_king, white_king_bishop, white_king_knight, white_king_rook):

                legel_moves = []


                legel_moves.append([white_king_knight[0] - 2, white_king_knight[1] + 1])
                legel_moves.append([white_king_knight[0] - 2, white_king_knight[1] - 1])

                legel_moves.append([white_king_knight[0] + 2, white_king_knight[1] + 1])
                legel_moves.append([white_king_knight[0] + 2, white_king_knight[1] - 1])

                legel_moves.append([white_king_knight[0] + 1, white_king_knight[1] + 2])
                legel_moves.append([white_king_knight[0] - 1, white_king_knight[1] + 2])

                legel_moves.append([white_king_knight[0] + 1, white_king_knight[1] - 2])
                legel_moves.append([white_king_knight[0] - 1, white_king_knight[1] - 2])

                legel_moves = [move for move in legel_moves if 1 <= move[0] <= 8 and 1 <= move[1] <= 8]




                if [button_chess_notation[i][0],button_chess_notation[i][1]] in legel_moves:

                    buttons[temperary_hold[0]].config(image=pixel)


                    if ((temperary_hold[0]//8)+(temperary_hold[0]%8)) % 2 == 0:
                        buttons[temperary_hold[0]].config(image=cream)

                    else:
                        buttons[temperary_hold[0]].config(image=green)

                    if (button_chess_notation[i][0]+button_chess_notation[i][1])%2 == 0:
                        print(123)
                        buttons[i].config(bg="#ffffcc")
                    else:
                        print(2345)
                        buttons[i].config(bg="#669933")

                    buttons[i].config(image=white_knight)
                    white_king_knight = button_chess_notation[i]
                    a = 0
                    temperary_hold=None


        if temperary_hold[1] == "wkr":
            if button_chess_notation[i] not in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                if white_king_rook[0] == button_chess_notation[i][0]:  # Same row
                    x = white_king_rook[1] - button_chess_notation[i][1]
                    if x < 0:  # Moving right
                        for number in range(1, -x + 1):
                            moves_to_check_wkr.append([white_king_rook[0], white_king_rook[1] + number])
                            if moves_to_check_wkr[number - 1] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                                break
                    elif x > 0:  # Moving left
                        for number in range(1, x + 1):
                            moves_to_check_wkr.append([white_king_rook[0], white_king_rook[1] - number])
                            if moves_to_check_wkr[number - 1] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                                break
                elif white_king_rook[1] == button_chess_notation[i][1]:  # Same column
                    x = white_king_rook[0] - button_chess_notation[i][0]
                    if x < 0:  # Moving down
                        for number in range(1, -x + 1):
                            moves_to_check_wkr.append([white_king_rook[0] + number, white_king_rook[1]])
                            if moves_to_check_wkr[number - 1] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                                break
                    elif x > 0:  # Moving up
                        for number in range(1, x + 1):
                            moves_to_check_wkr.append([white_king_rook[0] - number, white_king_rook[1]])
                            if moves_to_check_wkr[number - 1] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                                break

                if tuple(button_chess_notation[i]) in [tuple(move) for move in moves_to_check_wkr]:
                    print("Move is legal!")
                    buttons[temperary_hold[0]].config(image=pixel)

                    if ((temperary_hold[0]//8)+(temperary_hold[0]%8)) % 2 == 0:
                        buttons[temperary_hold[0]].config(image=cream)

                    else:
                        buttons[temperary_hold[0]].config(image=green)




                    buttons[i].config(image=white_rook)
                    if (button_chess_notation[i][0]+button_chess_notation[i][1])%2 == 0:
                        print(123)
                        buttons[i].config(bg="#ffffcc")
                    else:
                        print(2345)
                        buttons[i].config(bg="#669933")
                    a = 0
                    temperary_hold=None
                    white_king_rook = button_chess_notation[i]
            else: a=0


        elif temperary_hold[1] == "wkb":
            if abs(white_king_bishop[0] - button_chess_notation[i][0]) == abs(white_king_bishop[1] - button_chess_notation[i][1]):
                if white_king_bishop[0] - button_chess_notation[i][0] > 0 and white_king_bishop[1] - button_chess_notation[i][1] > 0:
                    for number in range(white_king_bishop[0] - button_chess_notation[i][0]):
                        moves_to_check_wkb.append([white_king_bishop[0] - number - 1, white_king_bishop[1] - number - 1])
                        if moves_to_check_wkb[number] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                            break


                elif white_king_bishop[0] - button_chess_notation[i][0] < 0 and white_king_bishop[1] - button_chess_notation[i][
                    1] < 0:
                    for number in range(abs(white_king_bishop[0] - button_chess_notation[i][0])):
                        moves_to_check_wkb.append([white_king_bishop[0] + number + 1, white_king_bishop[1] + number + 1])
                        if moves_to_check_wkb[number] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                            print(-1)
                            break

                elif white_king_bishop[0] - button_chess_notation[i][0] < 0 and white_king_bishop[1] - button_chess_notation[i][
                    1] > 0:
                    for number in range(abs(white_king_bishop[0] - button_chess_notation[i][0])):
                        moves_to_check_wkb.append([white_king_bishop[0] + number + 1, white_king_bishop[1] - number - 1])
                        if moves_to_check_wkb[number] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                            print(-1)
                            break

                elif white_king_bishop[0] - button_chess_notation[i][0] > 0 and white_king_bishop[1] - button_chess_notation[i][
                    1] < 0:
                    for number in range(abs(white_king_bishop[0] - button_chess_notation[i][0])):
                        moves_to_check_wkb.append([white_king_bishop[0] - number - 1, white_king_bishop[1] + number + 1])
                        if moves_to_check_wkb[number] in (
                    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7,
                    white_pawn8,
                    white_queen_rook, white_queen_knight, white_queen_bishop, white_queen_a,
                    white_king, white_king_bishop, white_king_knight, white_king_rook):
                            print(-1)
                            break

            if tuple(button_chess_notation[i]) in [tuple(move) for move in moves_to_check_wkb]:
                print("Move Is Legal!")
                buttons[temperary_hold[0]].config(image=pixel)

                if ((temperary_hold[0] // 8) + (temperary_hold[0] % 8)) % 2 == 0:
                    buttons[temperary_hold[0]].config(image=cream)

                else:
                    buttons[temperary_hold[0]].config(image=green)

                buttons[i].config(image=white_bishop)
                if (button_chess_notation[i][0] + button_chess_notation[i][1]) % 2 == 0:
                    print(123)
                    buttons[i].config(bg="#ffffcc")
                else:
                    print(2345)
                    buttons[i].config(bg="#669933")
                a = 0
                temperary_hold = None
                white_king_bishop = button_chess_notation[i]
            else:
                a = 0

        print(moves_to_check_wkb)

for i in range(64):
    row = i // 8
    column = i%8

    button = tk.Button(root, command=lambda i=i: button_click(i),width=100,height=100)
    button_chess_notation[i] = column+1,row+1

    buttons.append(button)
    if i not in button_numbers_with_pieces_at_start:
        if  (row + column) % 2 == 0:
            button.config(image=cream)
        else: button.config(image=green)

    else:
        if  (row + column) % 2 == 0:
            buttons[i].config(bg="#ffffcc")
        else: buttons[i].config(bg="#669933")
    button.grid(row=row,column=column)

buttons[1].config(image=white_knight)
buttons[6].config(image=white_knight)
buttons[62].config(image=black_knight   )
buttons[57].config(image=black_knight)
buttons[0].config(image=white_rook)
buttons[7].config(image=white_rook)
buttons[56].config(image=black_rook)
buttons[63].config(image=black_rook)
buttons[2].config(image=white_bishop)
buttons[5].config(image=white_bishop)
buttons[61].config(image=black_bishop)
buttons[58].config(image=black_bishop)
buttons[3].config(image=white_king_a)
buttons[59].config(image=black_king_a)
buttons[4].config(image=white_queen_image)
buttons[60].config(image=black_queen_image)

for i in range(8):
    buttons[8 + i].config(image=white_pawn)
    buttons[48 + i].config(image=black_pawn)

root.mainloop()