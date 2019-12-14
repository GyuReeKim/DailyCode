# 백준 14502번 - 연구소
# 푸는중

def bfs(r, c):
    global copy_lab
    copy_lab = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_lab[i][j] = lab[i][j]

    q.append((r, c))
    visited[r][c] = 1
    while q:
        r, c = q.pop(0)
        for k in range(4):
            nr = r + di[k]
            nc = c + dj[k]
            if 0 <= nr < N and 0 <= nc < M:
                if copy_lab[nr][nc] == 0 and visited[nr][nc] == 0:
                    copy_lab[nr][nc] = 2
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    print(copy_lab)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
print(lab)

places = []
for i in range(N):
    for j in range(M):
        places.append([i, j])
print(places)

maxV = 0
for i in range(len(places)-2):
    if lab[places[i][0]][places[i][1]] == 0:
        lab[places[i][0]][places[i][1]] = 1
        for j in range(i+1, len(places)-1):
            if lab[places[j][0]][places[j][1]] == 0:
                lab[places[j][0]][places[j][1]] = 1
                for k in range(j+1, len(places)):
                    if lab[places[k][0]][places[k][1]] == 0:
                        lab[places[k][0]][places[k][1]] = 1

                        q = []
                        visited = [[0]*M for _ in range(N)]
                        # print(lab)
                        for r in range(N):
                            for c in range(M):
                                if lab[r][c] == 2 and visited[r][c] == 0:
                                    bfs(r, c)
                        cnt = 0
                        for r in range(N):
                            for c in range(M):
                                if copy_lab[r][c] == 2:
                                    cnt += 1
                        if cnt > maxV:
                            maxV = cnt
                        lab[places[k][0]][places[k][1]] = 0
                lab[places[j][0]][places[j][1]] = 0
        lab[places[i][0]][places[i][1]] = 0
print(maxV)