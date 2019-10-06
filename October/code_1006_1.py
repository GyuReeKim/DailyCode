def f(i, j):
    global maze
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if maze[i][j] == '3':
        return 1
    else:
        maze[i][j] = '1'
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < 16 and nj >= 0 and nj < 16:
                if maze[ni][nj] != '1':
                    if f(ni, nj) == 1:
                        return 1
        return 0


T = 10
for tc in range(1, T+1):
    t = int(input())
    maze = [list(input()) for _ in range(16)]
    startI = 0
    startJ = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                startI = i
                startJ = j
                print('#{} {}'.format(tc, f(startI, startJ)))