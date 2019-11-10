# 백준 4963번 섬의 개수


def bfs(i, j):
    global land, q, visited, cnt
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    start = -1
    end = -1

    visited[i][j] = 1
    land[i][j] = 0
    end += 1
    q[end] = [i, j]

    while start != end:
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < h and nj >= 0 and nj < w and visited[ni][nj] == 0:
                if land[ni][nj] == 1:
                    visited[ni][nj] = visited[i][j] + 1
                    land[ni][nj] = 0
                    end += 1
                    q[end] = [ni, nj]
    cnt += 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    land = [list(map(int, input().split())) for _ in range(h)]
    q = ['']*w*h
    visited = [[0 for j in range(w)] for i in range(h)]
    # print(land)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                bfs(i, j)
                # print(visited)
    print(cnt)