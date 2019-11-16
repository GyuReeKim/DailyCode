# [모의 SW 역량테스트] 디저트 카페
# 수정 필요함


def find_square(I, J, visited, available_dessert, max_visited):
    visited_cnt = max_visited
    points = []
    while visited_cnt > 0:
        for i in range(N):
            for j in range(N):
                if visited[i][j] == visited_cnt:
                    points += [[i, j]]
        visited_cnt -= 1
    print(points)

    for i in range(1, 1<<len(points)):
        s = []
        e = []
        for j in range(len(points)):
            if i & (1<<j):
                s += [points[j]]
            else:
                e += [points[j]]
        if len(s) == 2:
            # print(s)
            is_point = 0
            for k in range(2):
                sideI, sideJ = I - s[k][0], J - s[k][1]
                # print(sideI, sideJ)
                for n in range(4):
                    for l in range(1, N):
                        if sideI == di[n]*l and sideJ == dj[n]*l:
                            # print(sideI, sideJ)
                            is_point += 1


def bfs(i, j):
    q = [''] * N * N

    visited = [[0] * N for _ in range(N)]
    available_dessert = [[0] * N for _ in range(N)]
    start, end = -1, -1
    dessert = []

    visited[i][j] = 1
    available_dessert[i][j] = cafe[i][j]
    dessert.append(cafe[i][j])
    end += 1
    q[end] = [i, j]

    max_visited = 0
    while start != end:
        start += 1
        si, sj = q[start][0], q[start][1]
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and available_dessert[ni][nj] == 0:
                # 겹치는 디저트가 없다면
                if cafe[ni][nj] not in dessert:
                    # print(cafe[ni][nj])
                    visited[ni][nj] = visited[si][sj] + 1
                    available_dessert[ni][nj] = cafe[ni][nj]
                    dessert.append(cafe[ni][nj])
                    end += 1
                    q[end] = [ni, nj]
                    if visited[ni][nj] > max_visited:
                        max_visited = visited[ni][nj]
    print(max_visited)
    print(startI, startJ)
    # print(dessert)
    pprint.pprint(visited, indent=4, width=N*10)
    find_square(startI, startJ, visited, available_dessert, max_visited)


# 방향을 총 3번 바꿀 수 있다.
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    exclude = [[0, 0], [0, N - 1], [N - 1, 0], [N - 1, N - 1]]
    maxV = -1
    for i in range(N):
        for j in range(N):
            if [i, j] not in exclude:
                startI, startJ = i, j
                bfs(startI, startJ)
    print('#{} {}'.format(tc, maxV))