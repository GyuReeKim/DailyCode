# 1953번 [모의 SW 역량테스트] 탈주범 검거

# 터널 구조물 타입
# # 1. right down left up : +
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# # 2. down up : |
# di = [1, -1]
# dj = [0, 0]
#
# # 3. right left : -
# di = [0, 0]
# dj = [1, -1]
#
# # 4. upright : ㄴ
# di = [-1, 0]
# dj = [0, 1]
#
# # 5. downright : r
# di = [0, 1]
# dj = [1, 0]
#
# # 6. downleft : ㄱ
# di = [1, 0]
# dj = [0, -1]
#
# # 7. upleft : J
# di = [0, -1]
# dj = [-1, 0]

ai = [[0, 1, 0, -1], [1, -1], [0, 0], [0, -1], [0, 1], [1, 0], [0, -1]]
aj = [[1, 0, -1, 0], [0, 0], [1, -1], [1, 0], [1, 0], [0, -1], [-1, 0]]
va = [
    [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]],
    [[1, 2, 4, 7], [1, 2, 5, 6]],
    [[1, 3, 6, 7], [1, 3, 4, 5]],
    [[1, 3, 6, 7], [1, 2, 5, 6]],
    [[1, 3, 6, 7], [1, 2, 4, 7]],
    [[1, 2, 4, 7], [1, 3, 4, 5]],
    [[1, 3, 4, 5], [1, 2, 5, 6]]
]


def bfs(i, j):
    global tunnel, q, visited
    start = -1
    end = -1

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]
    while start != end:
        # print(q)
        start += 1
        i = q[start][0]
        j = q[start][1]
        # print(i, j)
        # now는 tunnel 모양의 index 번호
        now = tunnel[i][j]-1
        di = ai[now]
        dj = aj[now]
        # tunnel[i][j]의 각 방향과 연결될 수 있는 모양의 리스트
        v = va[now]
        for k in range(len(di)):
            ni = i + di[k]
            nj = j + dj[k]
            vn = v[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0:
                if tunnel[ni][nj] in vn:
                    visited[ni][nj] = visited[i][j] + 1
                    end += 1
                    q[end] = [ni, nj]


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    # print(tunnel)
    q = ['']*N*M
    visited = [[0 for j in range(M)] for i in range(N)]

    for i in range(N):
        for j in range(M):
            if i == R and j == C:
                bfs(i, j)
    # print(tunnel)
    # print(visited)
    cnt = 0
    for r in range(N):
        for c in range(M):
            if 0 < visited[r][c] <= L:
                cnt += 1
    print('#{} {}'.format(tc, cnt))