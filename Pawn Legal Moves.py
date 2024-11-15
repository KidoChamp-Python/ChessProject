pawn_position = 2,2
new_pawn_position = 2,1
legal_moves = []
black_pieces = [(1,2),(3,2)]  # Example positions of white pieces
white_pieces = [(2,6)]

legal_moves.append([pawn_position[0],pawn_position[1]+1])
if tuple([pawn_position[0]-1,pawn_position[1]+1]) in black_pieces:
    legal_moves.append([pawn_position[0]-1,pawn_position[1]+1])
if tuple([pawn_position[0]+1,pawn_position[1]+1]) in black_pieces:
    legal_moves.append([pawn_position[0]+1,pawn_position[1]+1])

if pawn_position[0] == 2:
    if tuple([pawn_position[0],pawn_position[1]+1]) not in black_pieces:
        if tuple([pawn_position[0], pawn_position[1] + 1]) not in white_pieces:
            legal_moves.append([pawn_position[0], pawn_position[1]+2])

if tuple(new_pawn_position) in [tuple(move) for move in legal_moves]:
    print("Pawn move is Legal!")

print(legal_moves)
