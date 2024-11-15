knight_position = 2,1

legel_moves = []

legel_moves.append([knight_position[0] - 2, knight_position[1] + 1])
legel_moves.append([knight_position[0] - 2, knight_position[1] - 1])

legel_moves.append([knight_position[0] + 2, knight_position[1] + 1])
legel_moves.append([knight_position[0] + 2, knight_position[1] - 1])

legel_moves.append([knight_position[0] + 1, knight_position[1] + 2])
legel_moves.append([knight_position[0] - 1, knight_position[1] + 2])

legel_moves.append([knight_position[0] + 1, knight_position[1] - 2])
legel_moves.append([knight_position[0] - 1, knight_position[1] - 2])


legel_moves = [move for move in legel_moves if 1 <= move[0] <= 8 and 1 <= move[1] <= 8]


print(legel_moves)