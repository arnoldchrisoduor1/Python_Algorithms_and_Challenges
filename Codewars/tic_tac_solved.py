def is_solved(board):
    for i in range(3):
        #check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        #check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]
        
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    
    #chech if the board is not finished
    for row in board:
        if 0 in row:
            return -1 # board is not finished yet
    return 0 # cats game, draw