

def drawBoard(board, labels):
    """ Draws Game board """
##for row in board:
##    print(row)
##
##print(' 0 | 0 | 0 ') 
##print('---|---|---')
##print(' 0 | 0 | 0 ') 
##print('---|---|---')
##print(' 0 | 0 | 0 ')
    colNames, rowNames = labels
    print(' ')
    print(' '*10 +'C O L U M N')
    print(' '*11 +'{0}   {1}   {2}'.format(colNames[0],colNames[1],colNames[2]))
    print(' ')
    j = 0
    for row in board:
        x = ''
        for i in row:
            j += 1
            if j % 3 == 1:
                x +='Row {}'.format(rowNames[int(j/3)])+ ' '*5
            x += ' {0} '.format(i)
            if j % 3 != 0:
                x += '|'
            else:
                print
                print(x)
                if j != 9:
                    print((' '*10) +'---|---|---')
    print(' ')
    return

def checkWinner(board, plyr):
    """Checks for winner, given board and player"""
    winX = (plyr,plyr,plyr)
    winner = False

    for i in range(3):
        row = (board[i][0],board[i][1],board[i][2])
        if row == winX:
            winner = True
            break
        col = (board[0][i],board[1][i],board[2][i])
        if col == winX:
            winner = True
            break

    if not winner:
        leftDiag = (board[0][0],board[1][1],board[2][2])
        if leftDiag == winX:
            winner = True
        else:
            rightDiag = (board[0][2],board[1][1],board[2][0])
            if rightDiag == winX:
                winner = True
        
    return winner

def getMove(plyr, validMove, labels):
    move = 'Q'
    colNames, rowNames = labels
    
    if validMove:
        prompt = 'Your turn'
    else:
        prompt = 'Invalid! Try again'
    print (prompt+', Player '+plyr)
    col, row = 'Z', '9'
    try:
        while (len(col) != 1) or (col.upper() not in 'Q'+colNames):
            col = input('What Column, Player '+plyr+' ? ({0},{1},{2} or Q to quit): '.format(colNames[0],colNames[1],colNames[2]))
        col = col.upper()
        if col != 'Q':
            while (len(row) != 1) or (row.upper() not in 'Q'+rowNames):
                row = input('In Column '+col+', what Row Player '+plyr+' ? ({0},{1},{2} or Q to quit): '.format(rowNames[0],rowNames[1],rowNames[2]))
            row = row.upper()
            if row != 'Q':
                move = col+row
    except:
        print('OOOPS! error')
        
    return move

def parseMove(plyr, nextMove, board, labels):
    """ Parses the Move """
    goodMove = False
    blnk = ' '
    colNames, rowNames = labels
    
    if len(nextMove) == 2:
        colChoice, rowChoice = tuple(nextMove)
    colDic, rowDic = {}, {}
    try:
        for pair in enumerate(colNames):
            colDic[pair[1]] =  pair[0]
        col = colDic[colChoice]

        for pair in enumerate(rowNames):
            rowDic[pair[1]] =  pair[0]
        row = rowDic[rowChoice]
        
        if board[row][col] == blnk:
            board[row][col] = plyr
            goodMove = True
    except:
        print('OOOPS! error')
    return goodMove

def declareWinner(plyr):
    print(' ')
    print('Congratulations, Player '+plyr)
    print('You have WON!')
    print(' ')
    return


def sayBye():
    print(' ')
    print('Thanks for Playing.')
    print('Do play again!')
    print(' ')
    return

blnk = ' '
board = [[blnk,blnk,blnk],
        [blnk,blnk,blnk],
        [blnk,blnk,blnk]]
winner = False
goodMove = True
plyr = "O"
labels = ("ABC", "123")
colNames, rowNames = labels
while not winner: 
    drawBoard(board, labels)
    winner = checkWinner(board, plyr)
    if winner:
        declareWinner(plyr)
        nextMove = "Q"
    else:
        if goodMove:
            if plyr == "X":
                plyr = "O"
            else:
                plyr = "X"
        nextMove = getMove(plyr, goodMove, labels)
    if nextMove.upper() != 'Q':
        goodMove = parseMove(plyr, nextMove, board, labels)
    else:
        sayBye()
        winner = True
        
        
        
