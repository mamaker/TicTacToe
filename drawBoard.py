

def drawBoard(board, labels = ("ABC", "123")):
    """ Draws Game board """
##for row in board:
##    print(row)
##
##print(' 0 | 0 | 0 ') 
##print('---|---|---')
##print(' 0 | 0 | 0 ') 
##print('---|---|---')
##print(' 0 | 0 | 0 ')
#print(len(board[0]))
    colNames, rowNames = labels
    sideLen = len(colNames)
    boardLen = len(board)
    boardwidth = len(board[0])
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


board = [["0","0","0","0"],
         ["0","0","0","0"],
         ["0","0","0","0"],
         ["0","0","0","0"]]
drawBoard(board, labels = ("ABCD", "1234"))
