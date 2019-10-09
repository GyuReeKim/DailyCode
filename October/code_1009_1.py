# 혁진이의 프로그램 검증

# import sys
# sys.stdin=open('input.txt', 'r')


def f(i, j):
    global visited
    global d
    global memory
    global status
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    if visited[i][j] == 1:
        status = 'NO'
        return
    else:
        visited[i][j] = 1
        if table[i][j] in num:
            memory = int(table[i][j])
            f(i, j+1)
        elif table[i][j] == '>':
            d = 0
            nj = j + dj[d]
            if nj >= C:
                nj -= C
            f(i, nj)
        elif table[i][j] == 'v':
            d = 1
            ni = i + di[d]
            if ni >= R:
                ni -= R
            f(ni, j)
        elif table[i][j] == '<':
            d = 2
            nj = j + dj[d]
            if nj < 0:
                nj += C
            f(i, nj)
        elif table[i][j] == '^':
            d = 3
            ni = i + di[d]
            if ni < 0:
                ni += R
            f(ni, j)
        elif table[i][j] == '_':
            if memory == 0:
                d = 0
            else:
                d = 2
            nj = j + dj[d]
            if nj >= C:
                nj -= C
            elif nj < 0:
                nj += C
            f(i, nj)
        elif table[i][j] == '|':
            if memory == 0:
                d = 1
            else:
                d = 3
            ni = i + di[d]
            if ni >= R:
                ni -= R
            elif ni < 0:
                ni += R
            f(ni, j)
        elif table[i][j] == '?':
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if nj >= C:
                    nj -= C
                elif nj < 0:
                    nj += C
                elif ni >= R:
                    ni -= R
                elif ni < 0:
                    ni += R
                f(ni, nj)
        elif table[i][j] == '.':
            ni = i + di[d]
            nj = j + dj[d]
            f(ni, nj)
        elif table[i][j] == '@':
            status = 'YES'
            return
        elif table[i][j] == '+':
            memory += 1
            if memory > 15:
                memory -= 15
            ni = i + di[d]
            nj = j + dj[d]
            f(ni, nj)
        elif table[i][j] == '-':
            memory -= 1
            if memory < 0:
                memory += 15
            ni = i + di[d]
            nj = j + dj[d]
            f(ni, nj)


T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    table = [list(input()) for _ in range(R)]
    print(table)
    visited = [[0]*C for _ in range(R)]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    d = 0
    memory = 0
    status = ''
    f(0, 0)
    print('#{} {}'.format(tc, status))