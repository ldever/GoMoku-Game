import sys

class info:
    def __init__(self):
        self.color = '.'
        self.len = 0
        self.open = 1

def getInput():
    inFile = open(sys.argv[1],'r')
    global outFile 
    global task
    global player
    global d
    global n
    global board

    task = int(inFile.readline())
    player = int(inFile.readline())
    d = int(inFile.readline())
    n = int(inFile.readline())

    board = [list(line) for line in inFile]

def checkBound(i, j):
    if i >=0 and i < n and j >=0 and j < n:
        return True
    else:
        return False

def paraToIdx(createPara, openPara, lenPara):
    return createPara * 12 + openPara * 6 + lenPara

def evalFunc(currentColor, sign):
    val = 0
    for k in range(0,4):
        if check[k].color == '.':
            if check[k + 4].color == 'b':
                lenPara = check[k + 4].len + 1 * (currentColor == 'b')
                if lenPara > 5:
                    lenPara = 5
                createPara = 1 * (currentColor == 'b')
                openPara = check[k + 4].open
                idx = paraToIdx(createPara, openPara, lenPara)
                val = val + evalTable[idx] * sign
            if check[k + 4].color == 'w':
                lenPara = check[k + 4].len + 1 * (currentColor == 'w')
                createPara = 1 * (currentColor == 'w')
                openPara = check[k + 4].open
                idx = paraToIdx(createPara, openPara, lenPara)
                val = val + evalTable[idx] * sign
        if check[k].color == 'b':
            if check[k + 4].color == '.':
                lenPara = check[k].len + 1 * (currentColor == 'b')
                if lenPara > 5:
                    lenPara = 5
                createPara = 1 * (currentColor == 'b')
                openPara = check[k].open
                idx = paraToIdx(createPara, openPara, lenPara)
                val = val + evalTable[idx] * sign
            if check[k + 4].color == 'b':
                if (currentColor == 'b'):
                    lenPara = check[k].len + check[k + 4].len + 1
                    if lenPara > 5:
                        lenPara = 5
                    if check[k].open and check[k + 4].open:
                        openPara = 1
                    else:
                        openPara = 0
                    if check[k].open == 0 and check[k + 4].open == 0:
                        if not lenPara == 5:
                            lenPara = 0
                    createPara = 1
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                if (currentColor == 'w'):
                    lenPara = check[k].len
                    createPara = 0
                    openPara = check[k].open
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                    lenPara = check[k + 4].len
                    createPara = 0
                    openPara = check[k + 4].open
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
            if check[k + 4].color == 'w':
                if (currentColor == 'b'):
                    lenPara = check[k].len + 1
                    openPara = 0
                    if not check[k].open:
                        if not lenPara == 5:
                            lenPara = 0
                    createPara = 1
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                    lenPara = check[k + 4].len
                    openPara = check[k + 4].open
                    createPara = 0
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                if (currentColor == 'w'):
                    lenPara = check[k].len
                    openPara = check[k].open
                    createPara = 0
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                    lenPara = check[k + 4].len + 1
                    openPara = 0 #HHH
                    if not check[k + 4].open:
                        if not lenPara == 5:
                            lenPara = 0
                    createPara = 1
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
        if check[k].color == 'w':
            if check[k + 4].color == '.':
                lenPara = check[k].len + 1 * (currentColor == 'w')
                if lenPara > 5:
                    lenPara = 5
                createPara = 1 * (currentColor == 'w')
                openPara = check[k].open
                idx = paraToIdx(createPara, openPara, lenPara)
                val = val + evalTable[idx] * sign
            if check[k + 4].color == 'w':
                if (currentColor == 'w'):
                    lenPara = check[k].len + check[k + 4].len + 1
                    if lenPara > 5:
                        lenPara = 5
                    if check[k].open and check[k + 4].open:
                        openPara = 1
                    else:
                        openPara = 0
                    if check[k].open == 0 and check[k + 4].open == 0:
                        if not lenPara == 5:
                            lenPara = 0

                    createPara = 1
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                if (currentColor == 'b'):
                    lenPara = check[k].len
                    createPara = 0
                    openPara = check[k].open
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                    lenPara = check[k + 4].len
                    createPara = 0
                    openPara = check[k + 4].open
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
            if check[k + 4].color == 'b':
                if (currentColor == 'w'):
                    lenPara = check[k].len + 1
                    openPara = 0
                    if not check[k].open:
                        if not lenPara == 5:
                            lenPara = 0
                    createPara = 1
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                    lenPara = check[k + 4].len
                    openPara = check[k + 4].open
                    createPara = 0
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                if (currentColor == 'b'):
                    lenPara = check[k].len
                    openPara = check[k].open
                    createPara = 0
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
                    lenPara = check[k + 4].len + 1
                    openPara = 0
                    if not check[k + 4].open:
                        if not lenPara == 5:
                            lenPara = 0
                    createPara = 1
                    idx = paraToIdx(createPara, openPara, lenPara)
                    val = val + evalTable[idx] * sign
            
    return val

def greedy():
    global check
    value = [[0 for x in range(0,n)] for y in range(0,n)]

    outFile = open("next_state.txt", 'w')

    maxVal = 0
    if player==1:
        currentColor = 'b'
    else:
        currentColor = 'w'
    for j in range(0, n):    
        for i in reversed(range(0, n)):
            if board[i][j] == '.':
                check = [info() for x in range(0,8)]
                for k in range(0, 8):
                    nowi = i + dx[k]
                    nowj = j + dy[k]
                    if checkBound(nowi, nowj):  
                        check[k].color = board[nowi][nowj]
                        if not (check[k].color == '.'):
                            nowi = i + dx[k]
                            nowj = j + dy[k]
                            while checkBound(nowi, nowj) and board[nowi][nowj] == check[k].color:
                                check[k].len = check[k].len + 1
                                nowi = nowi + dx[k]
                                nowj = nowj + dy[k]
                            if (not checkBound(nowi, nowj)) or board[nowi][nowj] == '.':
                                check[k].open = 1
                            else:
                                check[k].open = 0
                val = evalFunc(currentColor, 1)
                value[i][j] = val
                if val > maxVal:
                    maxVal = val
                    maxi = i
                    maxj = j

    board[maxi][maxj] = currentColor
    for i in range(0, n):
        outFile.write("".join(board[i]))
    outFile.close()

def switch(currentColor):
    if currentColor == 'b':
        return 'w'
    else:
        return 'b'

def printMsg(currentD, i, j, value, sign):
    if (i == -1) and (j == -1):
        traverseFile.write("root,0,%s\n" % (trans(value)))
    else:
        traverseFile.write("%c%d,%d,%s\n" % (numToltr[j], n - i, currentD, trans(value)))


def dfs(currentD, currentColor, prev, sign, previ, prevj, win):
    global check
    global nexti
    global nextj


    if currentD >= d:
        printMsg(currentD, previ, prevj, prev, sign)                 
        return prev
    
    if win:
        printMsg(currentD, previ, prevj, prev, sign)
        return prev


    printMsg(currentD, previ, prevj, -sign * float("inf"), sign)
                    
    maxV = -float("inf")
    minV = float("inf")

    for j in range(0, n):
        for i in reversed(range(0, n)):
            if board[i][j] == '.':
                touch = 0
                check = [info() for x in range(0,8)]
                for k in range(0, 8):
                    nowi = i + dx[k]
                    nowj = j + dy[k]
                    if checkBound(nowi, nowj):  
                        check[k].color = board[nowi][nowj]
                        if not (check[k].color == '.'):
                            touch = 1
                            nowi = i + dx[k]
                            nowj = j + dy[k]
                            while checkBound(nowi, nowj) and board[nowi][nowj] == check[k].color:
                                check[k].len = check[k].len + 1
                                nowi = nowi + dx[k]
                                nowj = nowj + dy[k]
                            if (not checkBound(nowi, nowj)) or board[nowi][nowj] == '.':
                                check[k].open = 1
                            else:
                                check[k].open = 0
                if touch:
                    val = evalFunc(currentColor, sign)
                    board[i][j] = currentColor
                    prev = prev + val
                    if val <= -50000 or val >= 50000:
                        win = 1
                    else:
                        win = 0
                    v = dfs(currentD + 1, switch(currentColor), prev, -1 * sign, i, j, win)
                    if sign == 1:
                        if v > maxV:
                            if currentD == 0:
                                nexti = i
                                nextj = j
                            maxV = v
                        printMsg(currentD, previ, prevj, maxV, sign)
                    else:
                        if v < minV:
                            minV = v
                        printMsg(currentD, previ, prevj, minV, sign)
                    prev = prev - val
                    board[i][j] = '.'
    if sign == 1:
        return maxV
    else:
        return minV

def minimax():
    global traverseFile

    traverseFile = open("traverse_log.txt", 'w')
    traverseFile.write("Move,Depth,Value\n")
    nextFile = open("next_state.txt", 'w')

    if player == 1:
        currentColor = 'b'
    else:
        currentColor = 'w'
    sign = 1
    v = dfs(0, currentColor, 0, 1, -1, -1, 0)
    board[nexti][nextj] = currentColor
    currentColor = switch(currentColor)
    for i in range(0, n):
        nextFile.write("".join(board[i]))

    traverseFile.close()
    nextFile.close()

def trans(value):
    if value == -float("inf"):
        return "-Infinity"
    elif value == float("inf"):
        return "Infinity"
    else:
        return value

def printMsgAlphaBeta(currentD, i, j, value, sign, alpha, beta):
    if (i == -1) and (j == -1):
        traverseFile.write("root,0,%s,%s,%s\n" % (trans(value), trans(alpha), trans(beta)))
    else:
        traverseFile.write("%c%d,%d,%s,%s,%s\n" % (numToltr[j], n - i, currentD, trans(value), trans(alpha), trans(beta)))


def dfsPrune(currentD, currentColor, prev, sign, previ, prevj, win, alpha, beta):
    global check
    global nexti
    global nextj


    if currentD >= d:
        printMsgAlphaBeta(currentD, previ, prevj, prev, sign, alpha, beta)
        return prev
    
    if win:
        printMsgAlphaBeta(currentD, previ, prevj, prev, sign, alpha, beta)
        return prev


    printMsgAlphaBeta(currentD, previ, prevj, -sign * float("inf"), sign, alpha, beta)
                    
    maxV = -float("inf")
    minV = float("inf")

    for j in range(0, n):
        for i in reversed(range(0, n)):
            if board[i][j] == '.':
                touch = 0
                check = [info() for x in range(0,8)]
                for k in range(0, 8):
                    nowi = i + dx[k]
                    nowj = j + dy[k]
                    if checkBound(nowi, nowj):  
                        check[k].color = board[nowi][nowj]
                        if not (check[k].color == '.'):
                            touch = 1
                            nowi = i + dx[k]
                            nowj = j + dy[k]
                            while checkBound(nowi, nowj) and board[nowi][nowj] == check[k].color:
                                check[k].len = check[k].len + 1
                                nowi = nowi + dx[k]
                                nowj = nowj + dy[k]
                            if (not checkBound(nowi, nowj)) or board[nowi][nowj] == '.':
                                check[k].open = 1
                            else:
                                check[k].open = 0
                if touch:
                    val = evalFunc(currentColor, sign)
                    board[i][j] = currentColor
                    prev = prev + val
                    if val <= -50000 or val >= 50000:
                        win = 1
                    else:
                        win = 0
                    v = dfsPrune(currentD + 1, switch(currentColor), prev, -1 * sign, i, j, win, alpha, beta)
                    if sign == 1:
                        if v > maxV:
                            if currentD == 0:
                                nexti = i
                                nextj = j
                            maxV = v
                        if maxV >= beta:
                            board[i][j] = '.'
                            printMsgAlphaBeta(currentD, previ, prevj, maxV, sign, alpha, beta)
                            return maxV
                        if maxV > alpha:
                            alpha = maxV
                        printMsgAlphaBeta(currentD, previ, prevj, maxV, sign, alpha, beta)
                    else:
                        if v < minV:
                            minV = v
                        if minV <= alpha:
                            board[i][j] = '.'
                            printMsgAlphaBeta(currentD, previ, prevj, minV, sign, alpha, beta)
                            return minV
                        if minV < beta:
                            beta = minV   
                        printMsgAlphaBeta(currentD, previ, prevj, minV, sign, alpha, beta)
                    prev = prev - val
                    board[i][j] = '.'
    if sign == 1:
        return maxV
    else:
        return minV




def alphaBeta():
    global traverseFile

    traverseFile = open("traverse_log.txt", 'w')
    traverseFile.write("Move,Depth,Value,Alpha,Beta\n")
    nextFile = open("next_state.txt", 'w')

    if player == 1:
        currentColor = 'b'
    else:
        currentColor = 'w'
    sign = 1
    v = dfsPrune(0, currentColor, 0, 1, -1, -1, 0, -float("inf"), float("inf"))
    board[nexti][nextj] = currentColor
    currentColor = switch(currentColor)
    for i in range(0, n):
        nextFile.write("".join(board[i]))

    traverseFile.close()
    nextFile.close()

def main():
    global dx
    global dy
    global evalTable
    global numToltr
    numToltr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',' Y', 'Z']
    
    getInput()
    dx = [-1, -1, 0, 1, 1,  1,  0, -1]
    dy = [ 0,  1, 1, 1, 0, -1, -1, -1]
    evalTable = [0, 0, 0, 100, 10000, 0, 0, 0, 0, 500, 0, 0, 0, 0, 1, 10, 1000, 50000, 0, 0, 5, 50, 5000, 50000]

    if task == 1:
        greedy()
    if task == 2:
        minimax()
    if task == 3:
        alphaBeta()
    sys.exit(0)

if __name__  == "__main__":
	main()