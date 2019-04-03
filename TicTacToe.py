

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

    if not winner:
        rightDiag = (board[0][2],board[1][1],board[2][0])
        if rightDiag == winX:
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
        
        
        
