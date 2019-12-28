# 백준 7569번
# 시간초과

def f(h, i, j):
    q = []

    q.append((h, i, j))
    visited[h][i][j] = 1
    # print(q)

    while q:
        h, i, j = q.pop(0)
        # print(h, i, j)

        for l in range(3):
            nh = h + height[l]
            if 0 <= nh < H:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        # print(nh, ni, nj)
                        if box[nh][ni][nj] == '0' and visited[nh][ni][nj] == 0:
                            box[nh][ni][nj] = 1
                            q.append((nh, ni, nj))
                            visited[nh][ni][nj] = visited[h][i][j] + 1


height = [0, 1, -1]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

M, N, H = map(int, input().split())

box = [[list(input().split()) for i in range(N)] for h in range(H)]
# print(box)

visited = [[[0]*M for i in range(N)] for h in range(H)]
# print(visited)

already = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == '0':
                already += 1
# print(already)

result = 0
if already != 0:
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j] == '1' and visited[h][i][j] == 0:
                    f(h, i, j)
                elif box[h][i][j] == '-1':
                    visited[h][i][j] = -1
    # print(visited)

    maxV = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if visited[h][i][j] > maxV:
                    maxV = visited[h][i][j]
                if visited[h][i][j] == 0:
                    maxV = -1
                    break
            if maxV == -1:
                break
        if maxV == -1:
            break
    result = maxV
print(result)