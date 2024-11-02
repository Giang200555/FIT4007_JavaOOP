from pygame.examples.go_over_there import reset

from Rework import matrix

def Get_position_of_pawn(chessmanType, x, y, maxtrix):
    result = []
    if chessmanType < 0 and y != 1:
        if matrix[x][y-1] == 0:
            result.append([x, y-1])
            if (y == 7) and (matrix[x][y-2] == 0):
                result.append([x, y-2])
        if (x != 1) and (matrix[x-1][y-1] > 0):
            result.append([x-1, y-1])
        if (x != 8) and (matrix[x+1][y-1] > 0):
            result.append([x+1, y-1])
    elif chessmanType > 0 and y != 8:
        if matrix[x][y+1] == 0:
            result.append([x, y+1])
            if (y == 2) and (matrix[x][y+2] == 0):
                result.append([x, y+2])
        if (x!= 1) and (matrix[x-1][y+1] < 0):
            result.append([x-1, y+1])
        if (x!= 8) and (matrix[x+1][y+1] < 0):
            result.append([x+1, y+1])
    return result

def Get_positions_of_bishop(ChessmanType, x, y, xDir, yDir, maxtrix):
    result = []
    while True:
        x += xDir
        y += yDir
        if (x == 0) or (x == 9) or (y == 0) or (y == 9):
            break
        elif ChessmanType * matrix[x][y] > 0:
            break
        elif matrix[x][y] * ChessmanType < 0:
            result.append([x, y])
            break
        result.append([x, y])
    return result

def Get_positions_of_knight(direction, ChessmanType, x, y, xDir, yDir, maxtrix):
    result = []
    x += xDir
    y += yDir
    if direction == 'NB':
        if (y > 0) and (y < 9):
            if (x - 1 != 0):
                if (matrix[x -1][y] == 0):
                    result.append([x -1, y])
                elif (matrix[x -1][y] * ChessmanType < 0):
                    result.append([x -1, y])
            if (x + 1 != 9):
                if (matrix[x + 1][y] == 0):
                    result.append([x + 1, y])
                elif (matrix[x + 1][y] * ChessmanType < 0):
                    result.append([x + 1, y])

    if direction == 'DT':
        if (x > 0) and (x < 9):
            if (y - 1!= 0):
                if (matrix[x][y - 1] == 0):
                    result.append([x, y - 1])
                elif (matrix[x][y - 1] * ChessmanType < 0):
                    result.append([x, y - 1])
            if (y + 1 != 9):
                if (matrix[x][y + 1] == 0):
                    result.append([x, y + 1])
                elif (matrix[x][y + 1] * ChessmanType < 0):
                    result.append([x, y + 1])
    return result

def Get_positions_of_rook(ChessmanType, x, y, xDir, yDir, maxtrix):
    result = []
    while True:
        x += xDir
        y += yDir
        if (x == 0) or (x == 9) or (y == 0) or (y == 9):
            break
        elif ChessmanType * matrix[x][y] > 0:
            break
        elif matrix[x][y] * ChessmanType < 0:
            result.append([x, y])
            break
        result.append([x, y])
    return result

def Get_positions_of_king(ChessmanType, x, y, maxtrix):
    result = []
    xReal, yReal = (x, y)
    x, y = (xReal, yReal - 1)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])
    x, y = (xReal, yReal + 1)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])
    x, y = (xReal - 1, yReal)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])
    x, y = (xReal + 1, yReal)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])
    x, y = (xReal - 1, yReal - 1)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])
    x, y = (xReal + 1, yReal - 1)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])
    x, y = (xReal - 1, yReal + 1)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])
    x, y = (xReal + 1, yReal + 1)
    if (x != 0) and (x!= 9) and (y!= 0) and (y!= 9):
        if (matrix[x][y] * ChessmanType < 0) or (matrix[x][y] == 0):
            result.append([x, y])

    return result

def possiblePosition(chessman, x, y, maxtrix):
    result = [[x, y]]
    chessmanType = chessman
    if chessman < 0:
        chessman = -chessman
    if chessman == 1:
        res = Get_position_of_pawn(chessmanType, x, y, maxtrix)
        for index in res:
            result.append(index)

    if chessman == 2:
        res = [Get_positions_of_bishop(chessmanType, x, y, -1, -1, maxtrix),
               Get_positions_of_bishop(chessmanType, x, y, 1, -1, maxtrix),
               Get_positions_of_bishop(chessmanType, x, y, -1, 1, maxtrix),
               Get_positions_of_bishop(chessmanType, x, y, 1, 1, maxtrix),
               ]
        for i in res:
            for index in i:
                result.append(index)

    if chessman == 3:
        res = [Get_positions_of_knight('NB', chessmanType, x, y, 0, -2, maxtrix),
               Get_positions_of_knight('NB', chessmanType, x, y, 0, 2, maxtrix),
               Get_positions_of_knight('DT', chessmanType, x, y, 2, 0, maxtrix),
               Get_positions_of_knight('DT', chessmanType, x, y, -2, 0, maxtrix),
               ]
        for i in res:
            for index in i:
                result.append(index)

    if chessman == 4:
        res = [Get_positions_of_rook(chessmanType, x, y, 0, -1, maxtrix),
               Get_positions_of_rook(chessmanType, x, y, 0, 1, maxtrix),
               Get_positions_of_rook(chessmanType, x, y, 1, 0, maxtrix),
               Get_positions_of_rook(chessmanType, x, y, -1, 0, maxtrix),
               ]
        for i in res:
            for index in i:
                result.append(index)

    if chessman == 5:
        res = Get_positions_of_king(chessmanType, x, y, maxtrix)
        for index in res:
            result.append(index)

    if chessman == 6:
        # rook + bishop
        res = [Get_positions_of_rook(chessmanType, x, y, 0, -1, maxtrix),
               Get_positions_of_rook(chessmanType, x, y, 0, 1, maxtrix),
               Get_positions_of_rook(chessmanType, x, y, 1, 0, maxtrix),
               Get_positions_of_rook(chessmanType, x, y, -1, 0, maxtrix),
               Get_positions_of_bishop(chessmanType, x, y, -1, -1, maxtrix),
               Get_positions_of_bishop(chessmanType, x, y, 1, -1, maxtrix),
               Get_positions_of_bishop(chessmanType, x, y, -1, 1, maxtrix),
               Get_positions_of_bishop(chessmanType, x, y, 1, 1, maxtrix),
               ]
        for i in res:
            for index in i:
                result.append(index)

    return result

