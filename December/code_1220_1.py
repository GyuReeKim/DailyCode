# 백준 17135번 - 캐슬 디펜스
# 실패


def f(i, j):
    q = []
    visited = [[0]*M for _ in range(N)]

    visited[i][j] = 1
    if visited[i][j] <= D:
        if new_castle[i][j] == 1:
            delete[i][j] = 1
            return
    q.append((i, j))

    while q:
        i, j = q.pop(0)
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                if visited[ni][nj] <= D:
                    if new_castle[ni][nj] == 1:
                        delete[ni][nj] = 1
                        return
                q.append((ni, nj))


di = [0, 0, -1]
dj = [1, -1, 0]

N, M, D = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]

archer = [[0]*M]
# print(archer)
maxV = 0
for a in range(M-2):
    archer[0][a] = 2
    for b in range(a+1, M-1):
        archer[0][b] = 2
        for c in range(b+1, M):
            archer[0][c] = 2

            # castle 복사
            enemy = 0
            new_castle = [[0]*M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    new_castle[i][j] = castle[i][j]
                    if new_castle[i][j] == 1:
                        enemy += 1
            # print(enemy)
            cnt = 0
            while enemy != 0:

                delete = [[0]*M for _ in range(N)]

                for j in range(M):
                    if archer[0][j] == 2:
                        f(N-1, j)
                # print(delete)
                for i in range(N):
                    for j in range(M):
                        if delete[i][j] == 1:
                            new_castle[i][j] = 0
                            cnt += 1
                # print(cnt)

                new_castle = [[0]*M] + new_castle[:-1]
                # print(new_castle)

                enemy = 0
                for i in range(N):
                    for j in range(M):
                        if new_castle[i][j] == 1:
                            enemy += 1
            if cnt > maxV:
                maxV = cnt
            archer[0][c] = 0
        archer[0][b] = 0
    archer[0][a] = 0
print(maxV)