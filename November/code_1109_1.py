# 백준 1012번 유기농 배추

def bfs(i, j):
    global farm, q, visited, cnt
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    start = -1
    end = -1

    visited[i][j] = 1
    farm[i][j] = 0
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0:
                if farm[ni][nj] == 1:
                    visited[ni][nj] = 1
                    farm[ni][nj] = 0
                    end += 1
                    q[end] = [ni, nj]
    cnt += 1
    # print(cnt)


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    farm = [[0 for j in range(M)] for i in range(N)]
    for k in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1
    # print(farm)
    q = ['']*N*M
    # print(q)
    visited = [[0 for j in range(M)] for i in range(N)]
    # print(visited)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                bfs(i, j)
    print(cnt)