

def drawBoard(board):
    """ Draws Game board """
##for row in board:
##    print(row)
##
##print(' 0 | 0 | 0 ') 
##print('---|---|---')
##print(' 0 | 0 | 0 ') 
##print('---|---|---')
##print(' 0 | 0 | 0 ')
    print(' ')
    print(' '*10 +'C O L U M N')
    print(' '*11 +'A   B   C')
    print(' ')
    j = 0
    for row in board:
        x = ''
        for i in row:
            j += 1
            if j % 3 == 1:
                x +='Row {}'.format(int(j/3)+1)+ ' '*5
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
    (col1, col2, col3) = ([],[],[])
    (diag1, diag2) = ([],[])
    winner = False
    j = 1
    for row in board:
        if tuple(row) == winX:
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
            
    if not winner:
        if tuple(col1) == winX:
            winner = True
        elif tuple(col2) == winX:
            winner = True
        elif tuple(col3) == winX:
            winner = True

    if not winner:
        if tuple(diag1) == winX:
            winner = True
        elif tuple(diag2) == winX:
            winner = True
        
    return winner

def getMove(plyr, validMove):
    move = 'Q'
    if validMove:
        prompt = 'Your turn'
    else:
        prompt = 'Invalid! Try again'
    print (prompt+', Player '+plyr)
    try:
        col = input('What Column? (A,B,C or Q to quit) :')
        if col.upper() != 'Q':
            row = input('What Row? (1,2,3 or Q to quit)    :')
            if row.upper() != 'Q':
                move = col.upper()+row.upper()
    except:
        print('OOOPS! error')
        
    return move

def parseMove(plyr, nextMove, board):
    goodMove = False
    blnk = ' '
    try:
        if len(plyr) == 1 and len(nextMove) == 2:
            col = 'ABC'.index(nextMove[0])
            row = int(nextMove[1])-1
            if (row >=0 and row <= 2) and (col >=0 and col <= 2) and (board[row][col] == blnk):
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
while not winner: 
    drawBoard(board)
    winner = checkWinner(board,plyr)
    if winner:
        declareWinner(plyr)
        nextMove = "Q"
    else:
        if goodMove:
            if plyr == "X":
                plyr = "O"
            else:
                plyr = "X"
        nextMove = getMove(plyr, goodMove)
    if nextMove.upper() != 'Q':
        goodMove = parseMove(plyr, nextMove, board)
    else:
        sayBye()
        winner = True
        
        
        
