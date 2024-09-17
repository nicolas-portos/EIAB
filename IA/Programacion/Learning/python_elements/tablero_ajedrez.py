chess_white_piece = '♜♞♝♛♚♝♞♜♟'
chess_black_piece = '♖♘♗♕♔♗♘♖♙'

board = [[],[],[],[],[],[],[],[]]

def createBoard():
    for i in range(8):
        board[0].append(chess_white_piece[i]) # White Pieces
        board[1].append(chess_white_piece[8]) # White Pawns
        board[6].append(chess_black_piece[8]) # Blakc Pawns
        board[7].append(chess_black_piece[i]) # Black Pieces
        board[2].append(' ') # Empty space
        board[3].append(' ') # Empty space
        board[4].append(' ') # Empty space
        board[5].append(' ') # Empty space

def printBoard():
    num = 1
    for line in board:
        print(num,end=" ")
        for piece in line:
            print(piece,end = "  ")
        print()
        num +=1

    # Letters
    for i in range(8):
        print(f"  {chr(i+ord('A'))}",end="")

def movePiece():
    initial_position = list(input("\nIndique las coordenadas de la pieza que desee mover, ejemplo 'e5'\n"))
    next_position = list(input("Coordenadas del lugar al que quiere mover la pieza, ejemplo 'e6'\n"))
    
    # letter to num (column)
    initial_position[0] = ord(initial_position[0].upper())-65 
    next_position[0] = ord(next_position[0].upper())-65
    
    # Move Piece
    board[int(next_position[1])-1][next_position[0]] = board[int(initial_position[1])-1][initial_position[0]]
    board[int(initial_position[1])-1][initial_position[0]] = ' '

createBoard()
printBoard()

movePiece()
printBoard()