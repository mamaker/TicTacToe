

def drawBoard(board):
    """ Draws Game board """
##for row in game:
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


game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
board = [["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]]

drawBoard(board)
