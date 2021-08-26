def solution(m, n, board):
    new_board = []
    for i in board:
        new_board.append(list(i))
    board = new_board[:]
    breakBlock = []
    answer = 0
    while (True):
        for i in range(n):
            for j in range(m):
                breakBlock = checkBlock(j, i, board, breakBlock)

        if not breakBlock:
            break
        board = goDown(breakBlock, board, n, m)
        answer += len(breakBlock)
        breakBlock=[]

    return answer


def goDown(breakBlock, board, n, m):
    for point in breakBlock:
        board[point[0]][point[1]] = '0'

    for i in range(n):
        start = -1
        zero = -1
        for j in range(m-1,-1,-1):
            if board[j][i]=='0':
                if zero ==-1:
                    zero=j
            elif board[j][i].isalpha():
                if zero!=-1 and start==-1:
                    start=j

        for check in range(start,-1,-1):
            if board[check][i]!='0':
                board[zero][i]=board[check][i]
                zero -= 1

            board[check][i]='0'


    return board


def checkBlock(j, i, board, breakBlock):
    dx = [1, 1, 0]
    dy = [0, 1, 1]
    pivot = board[j][i]
    count = 0
    if pivot=='0':
        return breakBlock

    for k in range(3):
        if j + dx[k] < len(board) and i + dy[k] < len(board[0]):
            if board[j + dx[k]][i + dy[k]] == pivot:
                count += 1
    if count == 3:
        if [j, i] not in breakBlock:
            breakBlock.append([j, i])
        for k in range(3):
            if [j + dx[k], i + dy[k]] not in breakBlock:
                breakBlock.append([j + dx[k], i + dy[k]])

    return breakBlock


print( solution(6,6, ["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ])) #32