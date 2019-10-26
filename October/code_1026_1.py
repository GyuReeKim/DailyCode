# [S/W 문제해결 기본] 3일차 - 회문2

T = 10
for tc in range(1, T+1):
    t = int(input())
    N = 100
    board = [list(input()) for _ in range(N)]
    # print(board)

    maxV = 0
    for i in range(N):
        for j in range(N):
            row = ''
            for r in range(i, N):
                row += board[r][j]
                if row == row[::-1]:
                    if len(row) > maxV:
                        maxV = len(row)
            col = ''
            for c in range(j, N):
                col += board[i][c]
                if col == col[::-1]:
                    if len(col) > maxV:
                        maxV = len(col)
    print('#{} {}'.format(tc, maxV))