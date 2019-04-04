def checkWinner(board, plyr):
    """Checks for winner, given board and player"""
    winner = False
    winX = []
    sideLen = len(board)
    for i in range(sideLen):
        winX.append(plyr)
    winX = tuple(winX)
    print('WinX: {}'.format(winX))

    for row in board:
        print('Row :{0}'.format(row))
        if tuple(row) == winX:
            print('Winner: {}'.format(row))
            winner = True
            break

    for i in range(sideLen):
        col = []
        for j in range(sideLen):
            col.append(board[j][i])
        print('Col {0}'.format(col))
        if tuple(col) == winX:
            print('Winner: {}'.format(col))
            winner = True
            break

    if not winner:
        leftDiag = []
        for i in range(sideLen):
            leftDiag.append(board[i][i])
        print('left Diag:{}'.format(leftDiag))
        if tuple(leftDiag) == winX:
            print('Winner: {}'.format(leftDiag))
            winner = True
        else:
            rightDiag = []
            for i in range(sideLen):
                rightDiag.append(board[i][sideLen-1-i])
            print('right Diag:{}'.format(rightDiag))
            if tuple(rightDiag) == winX:
                print('Winner: {}'.format(rightDiag))
                winner = True
        
    return winner

plr = " "
##board = [[plr,plr,plr,plr],
##         ["X","X","X","X"],
##         [plr,plr,plr,plr],
##         [plr,plr,plr,plr]]
board = [[plr,"X",plr,plr],
         [plr,"X",plr,plr],
         [plr,"X",plr,plr],
         [plr,"X",plr,plr]]
##board = [[plr,plr,plr,"X"],
##         [plr,plr,"X",plr],
##         [plr,"X",plr,plr],
##         ["X",plr,plr,plr]]
##board = [["X",plr,plr,plr],
##         [plr,"X",plr,plr],
##         [plr,plr,"X",plr],
##         [plr,plr,plr,"X"]]
winner = checkWinner(board,"X")
print(winner)
