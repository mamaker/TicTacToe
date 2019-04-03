def checkWinner(board, plyr):
    """Checks for winner, given board and player"""
    winX = (plyr,plyr,plyr)
    winner = False
    print('WinX: {}'.format(winX))

    for i in range(3):
        row = (board[i][0],board[i][1],board[i][2])
        print('Row {0}:{1}'.format(i,row))
        if row == winX:
            print('Winner: {}'.format(row))
            winner = True
            break
        col = (board[0][i],board[1][i],board[2][i])
        print('Col {0}:{1}'.format(i,col))
        if col == winX:
            print('Winner: {}'.format(col))
            winner = True
            break

    if not winner:
        leftDiag = (board[0][0],board[1][1],board[2][2])
        print('left Diag:{}'.format(leftDiag))
        if leftDiag == winX:
            print('Winner: {}'.format(leftDiag))
            winner = True
        else:
            rightDiag = (board[0][2],board[1][1],board[2][0])
            print('right Diag:{}'.format(rightDiag))
            if rightDiag == winX:
                print('Winner: {}'.format(rightDiag))
                winner = True
        
    return winner

plr = " "
##board = [[plr,plr,plr],
##         ["X","X","X"],
##         [plr,plr,plr]]
##board = [[plr,"X",plr],
##         [plr,"X",plr],
##         [plr,"X",plr]]
board = [[plr,plr,"X"],
         [plr,"X",plr],
         ["X",plr,plr]]
##board = [[plr,plr,"X"],
##         [plr,plr,plr],
##         ["X",plr,"X"]]
winner = checkWinner(board,"X")
print(winner)
