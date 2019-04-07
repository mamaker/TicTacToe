""" Plays a game of Tic-Tac-Toe.
    Gameboard size Configurable dynamically;
    Players choose their own unique initials;
    Continue playing with a new game after one is over.
    (C) Madhu Vasudevan. 
"""

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
#        for col in colNames:
#            colHead += col+(' '*3)
        colHead = (' '*3).join(colNames)
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

    # check for row match
    for row in board:
        if tuple(row) == winX:
            winner = True
            break

    # check for column match
    for i in range(sideLen):
        col = []
        for j in range(sideLen):
            col.append(board[j][i])
        if tuple(col) == winX:
            winner = True
            break

    # check for diagonals match
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


def getMove(plyr, movesMade, labels = ("ABC", "123")):
    """Gets the player's next move.""" 

    move = ''
    colNames, rowNames = labels
    col, row = '', ''
    while move != 'Q' and move not in movesMade:
        if len(movesMade) == 0:
            prompt = 'Welcome'
        else:
            prompt = 'Your turn'
        if move != '':
            prompt = 'Invalid! Try again'
        
        move = 'Q'
    
        print(prompt+', Player',plyr)
        prompt = 'What Column, Player '+plyr+' ?'
        col = getChoice(prompt,colNames)
        if col != 'Q':
            prompt = 'In Column '+col+', what Row Player '+plyr+' ?'
            row = getChoice(prompt,rowNames)
            if row != 'Q':
                move = col+row
        if move != 'Q' and move not in movesMade:
            movesMade.add(move)
    

    return move


def makeMove(plyr, nextMove, board, labels = ("ABC", "123")):
    """ Parses the Move and 
        if good move
            updates the game board 
            and returns True """
    
    goodMove = False
    blnk = ' '
    colNames, rowNames = labels
    
    if len(nextMove) == 2:
        colChoice, rowChoice = tuple(nextMove)
        if colChoice in colNames and rowChoice in rowNames:
            try:
                col = colNames.index(colChoice)
                row = rowNames.index(rowChoice)            
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


def blankBoard(board, movesMade):
    """ Blank out the Gameboard 
        and blank out the movesMade set"""

    #Blank out the Gameboard
    blnk = ' '
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = blnk
    
    #blank out the movesMade set
    x = movesMade.copy()
    movesMade.difference_update(x)
            
    return True


def getChoice(prompt, options, showOptions = ''):
    """ Get input from User """

    choice = ''
    if showOptions == '':
        showOptions = options
    try:
        while (len(choice) != 1) or (choice.upper() not in tuple(options+'Q')):
            choice = input('{0} {1} or Q to quit: '.format(prompt,tuple(showOptions)))
    except:
        print('OOOPS! error')
        choice = 'Q'
        
    return choice.upper()


def getPlyrs():
    """Allow players to choose unique initials
        for markup of individuals's position in Gameboard"""

    letrs1 = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    showOpts = 'A>Z'
    prompt = 'What unique alphabet Initial for Player#'
    initl1 = ''
    while initl1 == '' or initl1 not in letrs1+'Q': 
        initl1 = getChoice(prompt+' 1?',letrs1, showOpts)

    if initl1 == 'A':
        showOpts = 'B>Z'
    elif initl1 == 'Z':
        showOpts = 'A>Y'
  
    try: 
        if initl1 != 'Q':
            x = list(letrs1)
            del x[x.index(initl1)]
            letrs2 = ''.join(x)
    except:
        print('OOOPS! error')
        letrs2 = letrs1        
    
    initl2 = initl1
    prompt = 'Except '+initl1+', '+prompt
    while initl1 != 'Q' and initl2 != 'Q' and  initl2 not in letrs2:
        initl2 = getChoice(prompt+' 2?',letrs2, showOpts)
        
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
            movesMade = set([])
            switchPlyr = {plr1:plr2,plr2:plr1}
            plyr = plr1
            nextMove = ''
            while nextMove != 'Q': 
                drawBoard(board, labels)
                nextMove = getMove(plyr, movesMade, labels)
                if nextMove != 'Q':
                    makeMove(plyr, nextMove, board, labels)
                    if checkWinner(board, plyr):
                        declareWinner(plyr, board, labels)
                        blankBoard(board, movesMade)
                        nextMove = getChoice('One more Game?','Yy')
                    plyr = switchPlyr[plyr]
    sayBye()
   
         
if __name__ == '__main__':
    main()
        
