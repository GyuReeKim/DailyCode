# 백준 16509번 장군


def bfs(i, j):
    di = [2, 3, 3, 2, -2, -3, -3, -2]
    dj = [3, 2, -2, -3, -3, -2, 2, 3]
    pi = [0, 1, 1, 2, 1, 2, 0, 1, 0, -1, -1, -2, -1, -2, 0, -1]
    pj = [1, 2, 0, 1, 0, -1, -1, -2, -1, -2, 0, -1, 0, 1, 1, 2]
    global visited, q, start, end

    visited[i][j] = 1
    end += 1
    q[end] = [i, j]
    # print(q)

    while start != end:
        # print(visited)
        # print(q)
        start += 1
        i = q[start][0]
        j = q[start][1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            xi_1 = i + pi[2*k]
            xj_1 = j + pj[2*k]
            xi_2 = i + pi[2*k+1]
            xj_2 = j + pj[2*k+1]
            if ni >= 0 and ni < N and nj >= 0 and nj < M and visited[ni][nj] == 0:
                if xi_1 >= 0 and xi_1 < N and xj_1 >= 0 and xj_1 < M:
                    if xi_2 >= 0 and xi_2 < N and xj_2 >= 0 and xj_2 < M:
                        if [xi_1, xj_1] != king and [xi_2, xj_2] != king:
                            visited[ni][nj] = visited[i][j] + 1
                            if [ni, nj] == king:
                                return visited[ni][nj] - 1
                            end += 1
                            q[end] = [ni, nj]
    return -1


user = list(map(int, input().split()))
king = list(map(int, input().split()))
N = 10
M = 9
visited = [[0 for j in range(M)] for i in range(N)]
# print(visited)
q = ['']*N*M
start = -1
end = -1

print(bfs(user[0], user[1]))