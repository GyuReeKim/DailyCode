# [S/W 문제해결 기본] 7일차 - 미로2

import sys
sys.stdin=open('input.txt', 'r')


def f(i, j):
    global N
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
            if ni >= 0 and ni < N and nj >= 0 and nj < N:
                if maze[ni][nj] != '1':
                    if f(ni, nj) == 1:
                        return 1
        return 0


T = 1
for tc in range(1, T+1):
    t = int(input())
    N = 100
    maze = [list(input()) for _ in range(N)]
    # print(maze)

    startI = 0
    startJ = 0
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print(f(startI, startJ))