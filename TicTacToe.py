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


def getMove(plyr, validMove, newGame, labels = ("ABC", "123")):
    """Gets the player's next move.""" 
    
    move = 'Q'
    colNames, rowNames = labels
    if newGame:
        prompt = 'Welcome'
    elif validMove:
        prompt = 'Your turn'
    else:
        prompt = 'Invalid! Try again'

    print(prompt+', Player',plyr)
    
    col, row = '', ''
    prompt = 'What Column, Player '+plyr+' ?'
    col = getChoice(prompt,colNames)
    if col != 'Q':
        prompt = 'In Column '+col+', what Row Player '+plyr+' ?'
        row = getChoice(prompt,rowNames)
        if row != 'Q':
            move = col+row

    return move

def makeMove(plyr, nextMove, board, labels = ("ABC", "123")):
    """ Parses the Move and 
        if good move
            update the game board 
            and return True """
    
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


def declareWinner(plyr, board, labels):
    """ declare Winner """
    
    drawBoard(board, labels)
    print(' ')
    print('Congratulations, Player',plyr)
    print('You have WON!')
    print(' ')
    return


def sayBye():
    """ Wish Goodbye """

    print(' ')
    print('Thanks for Trying.')
    print('Hope to see you again.')
    print(' ')
    return


def blankBoard(board):
    """ Blank out the Gameboard """

    blnk = ' '
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = blnk
            
    return True


def getChoice(prompt, options, showOptions = ''):
    """ Get input from User """

    choice = ''
    if showOptions == '':
        showOptions = options
    try:
        while (len(choice) != 1) or (choice.upper() not in tuple(showOptions+'Q')):
            choice = input('{0} {1} or Q to quit: '.format(prompt,tuple(showOptions)))
    except:
        print('OOOPS! error')
        choice = 'Q'
        
    return choice.upper()


def getChoice2(prompt, options):
    """ Get input from User """

    choice = ''
    try:
        while (len(choice) != 1) or (choice.upper() not in tuple(options+'Q')):
            choice = input('{0} {1} or Q to quit: '.format(prompt,tuple(options)))
    except:
        print('OOOPS! error')
        choice = 'Q'
        
    return choice.upper()


def getPlyrs():
    """Allow players to choose unique initials
        for markup of individuals's position in Gameboard"""

    letrs1 = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    showOpts = 'A>Z'
    prompt = 'What unique alphabet Initial, Player#'
    initl1 = ''
    while initl1 == '' or initl1 not in letrs1+'Q': 
        initl1 = getChoice(prompt+' 1?',letrs1, showOpts)

    if initl1 == 'A':
        showOpts = 'B>Z'
    elif initl1 == 'Z':
        showOpts = 'A>Y'
        
    x = list(letrs1+'Q')
    del x[x.index(initl1)]
    letrs2 = ''
    for letr in x:
        letrs2 += letr    
    
    initl2 = initl1
    while initl1 != 'Q' and initl2 != 'Q' and  (initl1 == initl2 or initl2 not in letrs2):
        initl2 = getChoice(prompt+' 2?',letrs2, showOpts)
        
    return initl1,initl2


def getPlyrs2():
    """Allow players to choose initials
        for markup of individuals's position in Gameboard"""
    
    letrs1 = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    prompt = 'What unique alphabet Initial, Player#'
    initl1 = getChoice(prompt+' 1?',letrs1)
    
    x = list(letrs1+'Q')
    del x[x.index(initl1)]
    letrs2 = ''
    for letr in x:
        letrs2 += letr    

    initl2 = initl1
    while initl1 != 'Q' and initl2 != 'Q' and  initl1 == initl2:
        initl2 = getChoice(prompt+' 2?',letrs2)
        
    return initl1,initl2

def getSize():
    """ Allow user to choose the Gameboard size
    from 3 to 9 square"""
    
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
        plr1, plr2 = getPlyrs()
    
        if plr1 != 'Q' and plr2 != 'Q':
            colNames = 'ABCDEFGHI'[:sideLen]
            rowNames = '123456789'[:sideLen]
            labels = (colNames, rowNames)
            blnk = ' '
            board = [[blnk for i in range(sideLen)] for j in range(sideLen)]
            switchPlyr = {plr1:plr2,plr2:plr1}
            plyr = plr1
            validMove = False
            newGame = True
            nextMove = ''
            while nextMove != 'Q': 
                drawBoard(board, labels)
                nextMove = getMove(plyr, validMove, newGame, labels)
                newGame = False
                if nextMove != 'Q':
                    validMove = makeMove(plyr, nextMove, board, labels)
                    if validMove: 
                        if checkWinner(board, plyr):
                            declareWinner(plyr, board, labels)
                            newGame = blankBoard(board)
                            nextMove = getChoice('One more Game?','Yy')
                        plyr = switchPlyr[plyr]
    sayBye()
   
         
if __name__ == '__main__':
    main()
        
