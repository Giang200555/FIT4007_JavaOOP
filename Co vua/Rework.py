import pygame, chess, math
from pygame.locals import *
import machinePlayer, process

pygame.init()
FPS = 120
fpsClock = pygame.time.Clock()

wScr, hScr = (800, 660)
win = pygame.display.set_mode((wScr, hScr))
pygame.display.set_caption('Chess with AI')
pygame.display.set_icon(pygame.image.load('./images/icon.jpg'))
board = chess.Board()

# Sound
# Get Image
bgFirst = pygame.image.load('./images/bg.jpg')
gameOverImg = pygame.image.load('./images/gameOver.png')
BoardImg = pygame.image.load('./images/board.jpg')
# Black player
pawBlack = pygame.image.load('./images/chess/bp.png')
knightBlack = pygame.image.load('./images/chess/bN.png')
bishopBlack = pygame.image.load('./images/chess/bB.png')
rookBlack = pygame.image.load('./images/chess/bR.png')
queenBlack = pygame.image.load('./images/chess/bQ.png')
kingBlack = pygame.image.load('./images/chess/bK.png')

# White player
pawWhite = pygame.image.load('./images/chess/wp.png')
knightWhite = pygame.image.load('./images/chess/wN.png')
bishopWhite = pygame.image.load('./images/chess/wB.png')
rookWhite = pygame.image.load('./images/chess/wR.png')
queenWhite = pygame.image.load('./images/chess/wQ.png')
kingWhite = pygame.image.load('./images/chess/wK.png')

Get_img_from_number = { 1: pawWhite,        -1: pawBlack,
                        2: knightWhite,     -2: knightBlack,
                        3: bishopWhite,     -3: bishopBlack,
                        4: rookWhite,       -4: rookBlack,
                        5: kingWhite,       -5: kingBlack,
                        6: queenWhite,      -6: queenBlack
                        }

Orange_block = pygame.Surface((80, 80), pygame.SRCALPHA)  # per-pixel alpha
Orange_block.fill((245, 190, 64, 128))  # notice the alpha value in the color

Red_block = pygame.Surface((80, 80))  # per-pixel alpha
Red_block.fill((255, 74, 77))

# 1: pawn, 2: knight, 3: bishop, 4: rook, 5: king, 6: queen

n = 9
matrix = [  # create matrix
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 1, 0, 0, 0, 0, 1, -4],
    [0, 3, 1, 0, 0, 0, 0, 1, -3],
    [0, 2, 1, 0, 0, 0, 0, 1, -2],
    [0, 6, 1, 0, 0, 0, 0, 1, -6],
    [0, 5, 1, 0, 0, 0, 0, 1, -5],
    [0, 2, 1, 0, 0, 0, 0, 1, -2],
    [0, 3, 1, 0, 0, 0, 0, 1, -3],
    [0, 4, 1, 0, 0, 0, 0, 1, -4]
]


def printMatrix():
    for y in range(1, 9):
        for x in range(1, 9):
            if matrix[y][x] >= 0:
                print(' ' + str(matrix[y][x]), + '  ', end='')
            else:
                print(str(matrix[y][x]) + '    ', end='')
        print()


# ------------------------
x_block = [0]
y_block = [0]


def get_location_of_each_block():
    global x_block, y_block
    lx = 10
    ly = 10
    for x in range(1, n):
        x_block.append(lx)
        lx += 80
    for y in range(1, n):
        y_block.append(ly)
        ly += 80


get_location_of_each_block()

ColorBackgroud = (40, 40, 40)
win.fill(ColorBackgroud)


def show_board_chess():
    win.blit(BoardImg, (40, 40))


# ------------------------ #text
def Draw_text(word, x, y, color, size):
    font = pygame.font.SysFont('Regular', size)
    text = font.render(word, True, color)
    win.blit(text, (x, y))
    if color == (28, 232, 212):
        WsizeText, HsizeText = text.get_size()
        if machine_turn:
            pygame.draw.line(win, (28, 232, 212), (x, y + 51), (x + WsizeText, y + 51), 3)


def show_text_turn():
    if player_turn:
        color1 = (28, 232, 212)
        color2 = (225, 225, 225)
    else:
        color1 = (225, 225, 225)
        color2 = (28, 232, 212)
    Draw_text('Player', wScr - 145, hScr - 100, color1, 50)
    Draw_text('Machine', wScr - 145, 100, color2, 50)


def show_chessman():
    for y in range(n):
        for x in range(n):
            if matrix[x][y] != 0:
                win.blit(Get_img_from_number[matrix[x][y]], (x_block[x], y_block[y]))


def Block_mouse_stay():
    if (10 <= xmouse <= 650) and (10 <= ymouse <= 650):
        for x in range(n):
            for y in range(n):
                if (x_block[x] <= xmouse <= x_block[x] + 80) and (y_block[y] <= ymouse <= y_block[y] + 80):
                    return [x, y]
    return [0, 0]


def Show_possiblePosition(ListPosition):
    for i in range(len(ListPosition)):
        x = ListPosition[i][0]
        y = ListPosition[i][1]
        win.blit(pos, (x_block[x], y_block[y]))


def NextClick():
    if Click1:
        return False, True
    else:
        return True, False


xChessman_moving_animation = 0
yChessman_moving_animation = 0
type_chessman = 'nothing'


def DrawTheMovingChessman(x0, y0, x1, y1):
    global xChessman_moving_animation, yChessman_moving_animation
    if x0 < x1:
        x0 += 10
    elif x0 > x1:
        x0 -= 10

    if y0 < y1:
        y0 += 10
    elif y0 > y1:
        y0 -= 10

    xChessman_moving_animation = x0
    yChessman_moving_animation = y0

    win.blit(type_chessman, (x0, y0))


def change_turn():
    global machine_turn, player_turn
    if player_turn:
        player_turn = False
        machine_turn = True
    else:
        player_turn = True
        machine_turn = False


def show_check_king():
    if isCheckmate:
        win.blit(Red_block, (x_block[xKing], y_block[yKing]))


def Convert_string_to_number(local):
    return [int(ord(local[0]) - 96), 9 - int(local[1])]


def Convert_number_to_string(local):
    return chr(local[0] + 96) + chr(9 - local[1] + 48)


def get_local_king(val):
    valKing = 5 * val
    for i in range(1, 9):
        if valKing in matrix[i]:
            y = matrix[i].index(valKing)
            x = i
            break
    return x, y


def move(local, lastValue):
    global matrix, board, localOfBlackKing, localOfWhiteKing
    moveForm = Convert_string_to_number(local[0] + local[1])
    moveTo = Convert_string_to_number(local[2] + local[3])

    # change value of
    matrix[moveTo[0]][moveTo[1]] = lastValue
    matrix[moveForm[0]][moveForm[1]] = 0

    # change in board
    MOVE = chess.Move.from_uci(local)
    board.push(MOVE)  # Make the move

    # change local if king
    if lastValue == -5:
        localOfBlackKing = moveTo
    elif lastValue == 5:
        localOfWhiteKing = moveTo

    pygame.draw.rect(win, ColorBackgroud, (wScr - 130, hScr // 2, 100, 30))
    Draw_text(local, wScr - 130, hScr // 2, (149, 222, 169), 40)


def show_block_last_move():
    if come != '':
        moveFrom = Convert_string_to_number(come[0] + come[1])
        moveTo = Convert_string_to_number(come[2] + come[3])
        win.blit(Orange_block, (x_block[moveFrom[0]], y_block[moveFrom[1]]))
        win.blit(Orange_block, (x_block[moveTo[0]], y_block[moveTo[1]]))


player_turn = True;
machine_turn = False;
moveFrom = [0, 0];
moveTo = [0, 0]
Click1 = False;
Click2 = False;
NotClick = True
listPossibleMove = []
moving = False
come = ''
isCheckmate = False
show_board_chess()
show_chessman()

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xmouse, ymouse = event.pos

    isClick, nothing1, nothing2 = pygame.mouse.get_pressed()

    Block_current = Block_mouse_stay()
    if player_turn and isClick and (10 <= xmouse <= 650) and (10 <= ymouse <= 650) and not moving:
        pygame.event.wait()
        Click1, Click2 = NextClick()

        if Click1 and (matrix[Block_current[0]][Block_current[1]] < 0):
            moveFrom = Block_current
            listPossibleMove = process.possiblePosition(matrix[moveFrom[0]][moveFrom[1]], moveFrom[0], moveFrom[1],
                                                        player_turn)
        else:
            Click1 = False; Click2 = True

        if Click2 and (Block_current in listPossibleMove):
            moveTo = Block_current
            if moveFrom != moveTo:
                come = Convert_number_to_string(moveFrom) + Convert_number_to_string(moveTo)
                move(come, matrix[moveFrom[0]][moveFrom[1]])
            R_moving_animation = 0
            type_Chessman = Get_img_from_number[matrix[moveTo[0]][moveTo[1]]]
            xChessman_moving_animation = x_block[moveFrom[0]]
            yChessman_moving_animation = y_block[moveFrom[1]]

            lastValue = matrix[moveFrom[0]][moveFrom[1]]
            matrix[moveFrom[0]][moveFrom[1]] = 0
            moving = True
            show_board_chess()
            show_chessman()

    if Click1:
        show_board_chess()
        Show_possiblePosition(listPossibleMove)
        show_block_last_move()
        show_check_king()
        show_chessman()

    if moving:
        if xChessman_moving_animation == x_block[moveTo[0]] and yChessman_moving_animation == y_block[moveTo[1]]:
            moving = False
            if moveFrom != moveTo:
                move(come, lastValue)
                change_turn()
            else:
                matrix[moveFrom[0]][moveFrom[1]] = lastValue

            show_board_chess()
            show_block_last_move()
            show_chessman()

            if board.is_check() and moveFrom != moveTo:
                isCheckmate = True
                val = matrix[moveTo[0]][moveTo[1]] // abs(matrix[moveTo[0]][moveTo[1]])
                xKing, yKing = get_local_king(val)
                show_check_king()
                show_chessman()
            else:
                isCheckmate = False

        else:
            show_board_chess()
            show_block_last_move()
            show_check_king()
            show_chessman()
            DrawTheMovingChessman(xChessman_moving_animation, yChessman_moving_animation, x_block[moveTo[0]],
                                  y_block[moveTo[1]])

    # machine_turn
    if machine_turn:
        show_board_chess()
        show_block_last_move()
        show_check_king()
        show_chessman()
        bestMove = machinePlayer.getBestMoveOfMachine(matrix, 3, True)
        come = bestMove
        moving = True
        moveFrom = Convert_string_to_number(bestMove[0] + bestMove[1])
        moveTo = Convert_string_to_number(bestMove[2] + bestMove[3])
        R_moving_animation = 0
        type_Chessman = Get_img_from_number[matrix[moveTo[0]][moveTo[1]]]
        lastValue = matrix[moveFrom[0]][moveFrom[1]]
        matrix[moveFrom[0]][moveFrom[1]] = 0
        xChessman_moving_animation = x_block[moveFrom[0]]
        yChessman_moving_animation = y_block[moveFrom[1]]
    machine_turn = False




pygame.quit()
