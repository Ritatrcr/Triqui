
def printBoard(matrix):
    print("""
    Board
          
     {}  | {}  | {} 
    ____________
     {}  | {}  | {} 
    ____________
     {}  | {}  | {} 
    """.format(*[cell for row in matrix for cell in row]))

def player(player):
    return 2 if player == 1 else 1

def check_win_next_move(board, player): #checks if in the next move the player can win
    # rows
    for row in board:
        if row.count(player) == 2 and row.count(' ') == 1:
            return True

    #columns
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(player) == 2 and column.count(' ') == 1:
            return True

    # diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]
    if diagonal1.count(player) == 2 and diagonal1.count(' ') == 1:
        return True
    if diagonal2.count(player) == 2 and diagonal2.count(' ') == 1:
        return True

    return False

def check_two_options(board, player): #checks if the player has two options to win
    cont=0
    # rows
    for row in board:
        if row.count(player) == 2 and row.count(' ') == 1:
            cont+=1

    # columns
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(player) == 2 and column.count(' ') == 1:
            cont+=1

    # diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]
    if diagonal1.count(player) == 2 and diagonal1.count(' ') == 1:
        cont+=1
    if diagonal2.count(player) == 2 and diagonal2.count(' ') == 1:
        cont+=1

    #if cont is 2 or greater, the player has two options to win
    if cont>=2:
        return True
    else:
        return False


def start():
    board = [[" " for _ in range(3)] for _ in range(3)]
    printBoard(board)
    current_player = 1
    moves_left = 9
    
    while True:
        print("Player", current_player, "'s Turn")

        try:
            # Solicitar al usuario que ingrese un número de celda
            cell = int(input("Enter the cell number (1-9): "))
            if 1 <= cell <= 9: #verifies if the cell number is in the range

                row, column = (cell - 1) // 3, (cell - 1) % 3#converts the cell number to row and column

                if board[row][column] not in ("X", "O"):#verifies if the cell is empty

                    board[row][column] = "X" if current_player == 1 else "O" #marks the cell with the player's symbol
                    printBoard(board)
                    
                    moves_left -= 1

                    #if the next player ha sthe chance to win, the game ends
                    if check_win_next_move(board, "X") and player(current_player) == 1:
                        print("Player 1 wins!")
                        break
                    elif check_win_next_move(board, "O") and player(current_player) == 2:    
                        print("Player 2 wins!")
                        break

                    
                    if moves_left <= 4:
                        if moves_left ==4 and check_two_options(board, "X") :
                            print("Player 1 already won!")
                            break
                        elif moves_left == 3 and check_win_next_move(board, "X"):
                            print("Player 1 already won!")
                            break
                        else:
                        #if there are no options of winning, then the game ends in a draw
                            print("Draw")
                            break    
                else:
                    print("Cell occupied, try again\n")
                    current_player = player(current_player)
            else:
                print("Cell number out of range, try again\n")
                current_player = player(current_player)
            current_player = player(current_player)
            
        except ValueError:
                print("Error: The input must be an integer\n")
        
start()