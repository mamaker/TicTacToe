def checkWinner(board, plyr):
    """Checks for winner, given board and player"""
    winX = (plyr,plyr,plyr)
    (col1, col2, col3) = ([],[],[])
    (diag1, diag2) = ([],[])
    winner = False
    j = 1
    print('WinX: {}'.format(winX))
    print('Rows')
    for row in board:
        print(tuple(row))
        if tuple(row) == winX:
            print('Winner: {}'.format(tuple(row)))
            winner = True
            break
        for col in row:
            if j % 3 == 1:
                col1.append(col)
                if j == 1:
                    diag1.append(col)
                elif j == 7:
                    diag2.append(col)
            elif j % 3 == 2:
                col2.append(col)
                if j == 5:
                    diag1.append(col)
                    diag2.append(col)
            else:
                col3.append(col)
                if j == 3:
                    diag2.append(col)
                elif j == 9:
                    diag1.append(col)
            j += 1
            
    print('Columns')
    print(tuple(col1))
    print(tuple(col2))
    print(tuple(col3))
        
    if not winner:
        if tuple(col1) == winX:
            print('Winner: {}'.format(tuple(col1)))
            winner = True
        elif tuple(col2) == winX:
            print('Winner: {}'.format(tuple(col2)))
            winner = True
        elif tuple(col3) == winX:
            print('Winner: {}'.format(tuple(col3)))
            winner = True

    print('Diagonals')
    print(tuple(diag1))
    print(tuple(diag2))
    if not winner:
        if tuple(diag1) == winX:
            print('Winner: {}'.format(tuple(diag1)))
            winner = True
        elif tuple(diag2) == winX:
            print('Winner: {}'.format(tuple(diag2)))
            winner = True
        
    return winner

plr = "0"
##board = [[plr,plr,plr],
##         ["X","X","X"],
##         [plr,plr,plr]]
##board = [[plr,"X",plr],
##         [plr,"X",plr],
##         [plr,"X",plr]]
##board = [[plr,plr,"X"],
##         [plr,"X",plr],
##         ["X",plr,plr]]
board = [[plr,plr,"X"],
         [plr,plr,plr],
         ["X",plr,"X"]]
winner = checkWinner(board,"X")
print(winner)
