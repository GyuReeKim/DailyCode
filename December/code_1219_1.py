# 백준 17070번 - 파이프 옮기기1

def f(i, j, d):
    global cnt
    if i == N-1 and j == N-1:
        cnt += 1
    else:
        if d == 0:
            if j+1 < N and house[i][j+1] == 0:
                f(i, j+1, 0)
            if i+1 < N and j+1 < N and house[i+1][j+1] == house[i+1][j] == house[i][j+1] == 0:
                f(i+1, j+1, 2)
        if d == 1:
            if i+1 < N and house[i+1][j] == 0:
                f(i+1, j, 1)
            if i+1 < N and j+1 < N and house[i+1][j+1] == house[i+1][j] == house[i][j+1] == 0:
                f(i+1, j+1, 2)
        if d == 2:
            if j+1 < N and house[i][j+1] == 0:
                f(i, j+1, 0)
            if i+1 < N and house[i+1][j] == 0:
                f(i+1, j, 1)
            if i+1 < N and j+1 < N and house[i+1][j+1] == house[i+1][j] == house[i][j+1] == 0:
                f(i+1, j+1, 2)


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
# print(house)

cnt = 0
f(0, 1, 0)
print(cnt)