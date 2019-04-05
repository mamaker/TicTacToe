""" Plays a game of Tic-Tac-Toe.
    Gameboard size Configurable dynamically."""

def drawBoard(board, labels = ("ABC", "123")):
    """ Draws Game board """
##
##print(' X | O | O ') 
##print('---|---|---')
##print(' O | X | O ') 
##print('---|---|---')
##print(' O | O | X ')
#
    colNames, rowNames = labels
    sideLen = len(colNames)

    lhs = (sideLen, sideLen, sideLen)
    rhs = (len(rowNames), len(board), len(board[0]))
    if lhs == rhs:
        print(' ')
        print(' '*10 +'C O L U M N S')
        colHead = ''
        for col in colNames:
            colHead += col+(' '*3)
        print(' '*11 +colHead)
            
        print(' ')
        j = 0
        for row in board:
            x = ''
            for i in row:
                j += 1
                if j % sideLen == 1:
                    x +='Row {}'.format(rowNames[int(j/sideLen)])+ ' '*5
                x += ' {0} '.format(i)
                if j % sideLen != 0:
                    x += '|'
                else:
                    print(x)
                    if j != sideLen**2:
                        divider = (' '*10)
                        for k in range(sideLen):
                            divider += '---'
                            if k < sideLen -1:
                                divider += '|'
                        print(divider)
        print(' ')

    else:
        print('Sorry, can only draw square gameboards.')
    return

def checkWinner(board, plyr):
    """Checks for winner, given board and player"""
    winner = False
    winX = []
    sideLen = len(board)
    for i in range(sideLen):
        winX.append(plyr)
    winX = tuple(winX)

    for row in board:
        if tuple(row) == winX:
            winner = True
            break

    for i in range(sideLen):
        col = []
        for j in range(sideLen):
            col.append(board[j][i])
        if tuple(col) == winX:
            winner = True
            break

    if not winner:
        leftDiag = []
        for i in range(sideLen):
            leftDiag.append(board[i][i])
        if tuple(leftDiag) == winX:
            winner = True
        else:
            rightDiag = []
            for i in range(sideLen):
                rightDiag.append(board[i][sideLen-1-i])
            if tuple(rightDiag) == winX:
                winner = True
        
    return winner

def getMove(plyr, validMove, labels = ("ABC", "123")):
    """Gets the player's next move.""" 
    
    move = 'Q'
    colNames, rowNames = labels
    prompt = 'Invalid! Try again'
    if validMove:
        prompt = 'Your turn'
    print (prompt,', Player',plyr)
    col, row = '', ''
    prompt = 'What Column, Player '+plyr+' ?'
    col = getChoice(prompt,colNames)
    if col != 'Q':
        prompt = 'In Column '+col+', what Row Player '+plyr+' ?'
        row = getChoice(prompt,rowNames)
        if row != 'Q':
            move = col+row

    return move

def parseMove(plyr, nextMove, board, labels = ("ABC", "123")):
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
    print('Congratulations, Player',plyr)
    print('You have WON!')
    print(' ')
    return


def sayBye():
    print(' ')
    print('Thanks for Playing.')
    print('Do play again!')
    print(' ')
    return

def getChoice(prompt, options):
    choice = ''
    try:
        while (len(choice) != 1) or (choice.upper() not in tuple(options+'Q')):
            choice = input('{0} {1} or Q to quit: '.format(prompt,tuple(options)))
    except:
        print('OOOPS! error')
        choice = 'Q'
        
    return choice.upper()

def getSize():
    size = 0
    sizes = '3456789'
    siz = getChoice('What size Game board?', sizes)
    
    if len(siz) == 1 and siz != 'Q':
        size = int(siz)

    return size


def main():
    """ Plays a game of Tic-Tac-Toe.
        Gameboard size Configurable dynamically."""
    #sideLen = 4
    sideLen = getSize()
    if sideLen > 2 and sideLen < 10:
        blnk = ' '
        board = [[blnk for i in range(sideLen)] for j in range(sideLen)]
    
        colNames = 'ABCDEFGHI'[:sideLen]
        rowNames = '123456789'[:sideLen]
    
        labels = (colNames, rowNames)
        winner = not (len(colNames) == len(rowNames))
        goodMove = True
        plyr = "O"
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
            
    else:
        print('Sorry, Hope to see you again.')
   
         
if __name__ == '__main__':
    main()
        
