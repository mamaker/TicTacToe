def parseMove(plyr, nextMove, board):
    try:
        #print(plyr)
        #print(nextMove)
        if len(plyr) == 1 and len(nextMove) == 2:
            col = 'ABC'.index(nextMove[0])
            #print(col)
            row = int(nextMove[1])-1
            #print(row)
            if (row >=0 and row <= 2) and (col >=0 and col <= 2):
                board[row][col] = plyr
    except:
        print('error')
    return board
              
board = [["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]]
plyr = "X"
nextMove = "C2"
board = parseMove(plyr, nextMove, board)

for row in board:
    print(row)              
