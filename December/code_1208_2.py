# 백준 17822번 - 원판 돌리기
# 런타임 에러


def find(i, j):
    global plates, cnt
    change_cnt = 0
    q = ['']*N*M
    visited = [[0]*M for _ in range(N)]
    start = -1
    end = -1

    end += 1
    q[end] = [i, j]
    visited[i][j] = 1

    while start != end:
        start += 1
        qi = q[start][0]
        qj = q[start][1]
        for kk in range(4):
            ni = qi + di[kk]
            nj = qj + dj[kk]
            if nj < 0:
                nj += M
            elif nj >= M:
                nj -= M
            if ni >= 0 and ni < N:
                if visited[ni][nj] == 0 and plates[ni][nj] == origin:
                    plates[ni][nj] = 'x'
                    end += 1
                    q[end] = [ni, nj]
                    visited[ni][nj] = 1
                    change_cnt += 1
                    # print(plates)
    
    if change_cnt != 0:
        cnt += 1
        plates[i][j] = 'x'
        # print(plates)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M, T = map(int, input().split())
plates = []
for n in range(N):
    plate = list(map(int, input().split()))
    plates.append(plate)
# print(plates)

result = 0
for t in range(T):
    x, d, k = map(int, input().split())
    # print(plates)

    # 회전
    for n in range(N):
        if (n+1) % x == 0:
            temp = plates[n]
            if d == 0:
                for kk in range(k):
                    left = temp[:-1]
                    right = temp[-1:]
                    temp = right + left
            elif d == 1:
                for kk in range(k):
                    left = temp[:1]
                    right = temp[1:]
                    temp = right + left
            plates[n] = temp
    # print('회전')
    # print(plates)

    # 인접 찾기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if plates[i][j] != 'x':
                origin = plates[i][j]
                # print(origin)
                find(i, j)
    # print('인접')
    # print(plates)
    # print(cnt)

    # 인접 없는 경우
    add = 0
    if cnt == 0:
        num_cnt = 0
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 'x':
                    add += plates[i][j]
                    num_cnt += 1
        average = add / num_cnt
        # print(plates)

        for i in range(N):
            for j in range(M):
                if plates[i][j] != 'x':
                    if plates[i][j] < average:
                        plates[i][j] += 1
                        add += 1
                    elif plates[i][j] > average:
                        plates[i][j] -= 1
                        add -= 1
    if cnt != 0:
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 'x':
                    add += plates[i][j]
    # print(plates)
    # print(add)
    if t == T-1:
        result = add
print(result)