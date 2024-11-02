import process
from Rework import moveFrom, matrix


def Convert_string_to_number(local):
    return [ord(local[0]) - 96, 9 - int(local[1])]

def Convert_number_to_string(local):
    return chr(local[0] + 96) + chr(9 - local[1] + 48)

def get_all_move(chessmans, ways):
    result = []
    for i in range(len(chessmans)):
        moveFrom = chessmans[i]
        for j in range(len(ways[i])):
            moveTo = ways[i][j]
            result.append(Convert_number_to_string(moveFrom) + Convert_number_to_string(moveTo))
    return result

def get_value(chessman):
    chessmanType = chessman
    value = 0
    chessman = abs(chessman)

    if chessman == 1:
        value = 10
    elif chessman == 2 or chessman == 3:
        value = 30
    elif chessman == 4:
        value = 50
    elif chessman == 5:
        value = 900
    elif chessman == 6:
        value = 90

    if chessmanType < 0:
        return value
    else:
        return -value

def moveNotReal(moveChar, Newmatrix):
    localBefore = [ord(moveChar[0]) - 96, 9 - int(moveChar[1])]
    localAfter = [ord(moveChar[2]) - 96, 9 - int(moveChar[3])]
    valueChessman = Newmatrix[localBefore[0]][localBefore[1]]
    Newmatrix[localBefore[0]][localBefore[1]] = 0
    Newmatrix[localAfter[0]][localAfter[1]] = valueChessman
    return Newmatrix

def get_all_move(chessmans, ways):
    result = []
    for i in range(len(chessmans)):
        moveFrom = chessmans[i]
        for j in range(len(ways[i])):
            moveTo = ways[i][j]
            result.append(Convert_number_to_string(moveFrom) + Convert_number_to_string(moveTo))
    return result

def Convert_string_to_number(local):
    return [ord(local[0]) - 96, 9 - int(local[1])]

def Undo(matrix, moveCome, lastValueMatrix):
    moveBack = moveCome[2] + moveCome[3] + moveCome[0] + moveCome[1]
    moveNotReal(moveBack, matrix)
    moveTo = Convert_string_to_number(moveCome[2:])
    matrix[moveTo[0]][moveTo[1]] = lastValueMatrix
    return matrix

def get_ways(maxtrix, isPlayer):
    chessmanOfMachine = []
    all_ways = []
    for y in range(1, 9):
        for x in range(1, 9):
            if isPlayer and maxtrix[x][y] < 0:
                chessmanOfMachine.append([x, y])
                all_ways.append(process.possiblePosition(matrix[x][y], x, y, maxtrix))
            elif not isPlayer and maxtrix[x][y] > 0:
                chessmanOfMachine.append([x, y])
                all_ways.append(process.possiblePosition(matrix[x][y], x, y, maxtrix))
        return chessmanOfMachine, all_ways

def get_value_of_all_matrix(matrix):
    value = 0
    for y in range(1, 9):
        for x in range(1, 9):
            if matrix[x][y]!= 0:
                value += get_value(matrix[x][y])
    return value

def get_local_king(val):
    valKing = 5 * val
    for i in range(1, 9):
        if valKing in matrix[i]:
            y = matrix[i].index(valKing)
            x = i
            break
    return x, y

def minimax(deep, matrixNew, alpha, beta, isMaximisingPlayer):
    global  time
    time += 1

    if deep == 0:
        return -get_value_of_all_matrix(matrixNew)

    chessmans, ways = get_ways(matrixNew, not isMaximisingPlayer)
    moves = get_all_move(chessmans, ways)

    if isMaximisingPlayer:
        besrValue = -9999
        for i in range(len(moves)):
            moveTo = Convert_string_to_number(moves[i][2:])
            lastValueInMatrix = matrixNew[moveTo[0]][moveTo[1]]
            matrixNew = moveNotReal(moves[i], matrixNew)
            bestValue = max(bestValue, minimax(deep - 1, matrixNew, alpha, beta, not isMaximisingPlayer))
            matrixNew = Undo(matrixNew, moves[i], lastValueInMatrix)

            alpha = max(alpha, bestValue)
            if beta <= alpha:
                return bestValue
        return bestValue
    else:
        bestValue = 9999
        for i in range(len(moves)):
            moveTo = Convert_string_to_number(moves[i][2:])
            lastValueInMatrix = matrixNew[moveTo[0]][moveTo[1]]
            matrixNew = moveNotReal(moves[i], matrixNew)
            bestValue = min(bestValue, minimax(deep - 1, matrixNew, alpha, beta, not isMaximisingPlayer))
            matrixNew = Undo(matrixNew, moves[i], lastValueInMatrix)

            beta = min(beta, bestValue)
            if beta <= alpha:
                return bestValue
        return bestValue

time = 0

def getBestMoveOfMachine(matrix, deep, isMaximisingPlayer):
    global time
    time = 0
    chessmans, ways = get_ways(matrix, not isMaximisingPlayer)
    all_move = get_all_move(chessmans, ways)
    bestMoveValue = -9999
    bestMoveFound =''
    for  i in range(len(all_move)):
        moveTo = Convert_string_to_number(all_move[i][2:])
        lastValueInMatrix = matrix[moveTo[0]][moveTo[1]]
        matrix = moveNotReal(all_move[i], matrix)

        value = minimax(deep - 1, matrix, -10000, 10000, not isMaximisingPlayer)
        matrix = Undo(matrix, all_move[i], lastValueInMatrix)

        if value >= bestMoveValue:
            bestMoveValue = value
            bestMoveFound = all_move[i]

    print('Number Comparations:', time)
    return bestMoveFound



