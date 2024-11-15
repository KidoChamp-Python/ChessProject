bishop_position = 5,5
new_bishop_position = 8,2
moves_to_check= []
white_pieces = [(1,5),(1,2)]  # Example positions of white pieces

if abs(bishop_position[0] - new_bishop_position[0]) == abs(bishop_position[1] - new_bishop_position[1]):
    if bishop_position[0] - new_bishop_position[0] > 0 and bishop_position[1]-new_bishop_position[1]>0:
        for number in range(bishop_position[0]-new_bishop_position[0]):
            moves_to_check.append([bishop_position[0]-number-1,bishop_position[1]-number-1])
            if tuple(moves_to_check[number]) in white_pieces:
                moves_to_check.remove(moves_to_check[-1])
                break


    elif bishop_position[0] - new_bishop_position[0] < 0 and bishop_position[1]-new_bishop_position[1] < 0:
        for number in range(abs(bishop_position[0] - new_bishop_position[0])):
            moves_to_check.append([bishop_position[0] + number + 1, bishop_position[1] + number + 1])
            if tuple(moves_to_check[number]) in white_pieces:
                moves_to_check.remove(moves_to_check[-1])
                print(-1)
                break

    elif bishop_position[0] - new_bishop_position[0] < 0 and bishop_position[1] - new_bishop_position[1] > 0:
        for number in range(abs(bishop_position[0] - new_bishop_position[0])):
            moves_to_check.append([bishop_position[0] + number + 1, bishop_position[1] - number - 1])
            if tuple(moves_to_check[number]) in white_pieces:
                moves_to_check.remove(moves_to_check[-1])

                print(-1)
                break

    elif bishop_position[0] - new_bishop_position[0] > 0 and bishop_position[1] - new_bishop_position[1] <0:
        for number in range(abs(bishop_position[0] - new_bishop_position[0])):
            moves_to_check.append([bishop_position[0] - number - 1, bishop_position[1] + number + 1])
            if tuple(moves_to_check[number]) in white_pieces:
                moves_to_check.remove(moves_to_check[-1])
                print(-1)
                break


if tuple(new_bishop_position) in [tuple(move) for move in moves_to_check]:
    print("Move Is Legal!")

print(moves_to_check)