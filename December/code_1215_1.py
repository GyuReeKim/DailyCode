# 백준 14502번 - 연구소

def f(n, m, k, l):
    global copy_lab, visited, maxV
    if n == l:
        # print(choice)
        copy_lab = [[0]*M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                if (r, c) in choice:
                    copy_lab[r][c] = 1
                else:
                    copy_lab[r][c] = lab[r][c]
        visited = [[0]*M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                if copy_lab[r][c] == 2 and visited[r][c] == 0:
                    bfs(r, c)
        cnt = 0
        for r in range(N):
            for c in range(M):
                if copy_lab[r][c] == 0:
                    cnt += 1
        if cnt > maxV:
            maxV = cnt
    else:
        for i in range(m, k-(l-n)+1):
            choice[n] = wall_list[i]
            f(n+1, i+1, k, l)


def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if copy_lab[ni][nj] == 0:
                    copy_lab[ni][nj] = 2
                    q.append((ni, nj))
                    visited[ni][nj] = 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

k = 0
wall_list = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            k += 1
            wall_list.append((i, j))
choice = [0]*3
maxV = 0
f(0, 0, k, 3)
print(maxV)