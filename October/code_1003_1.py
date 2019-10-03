# [S/W 문제해결 기본] 5일차 - Magnetic

def f(i, j):
    if table[i][j] == 2:
        return 1
    else:
        ni = i+1
        if ni < N:
            if table[ni][j] == 1:
                return 0
            else:
                if f(ni, j) == 1:
                    return 1
        return 0


T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                if f(i, j) == 1:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))