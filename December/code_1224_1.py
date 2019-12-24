# 백준 14501번 - 퇴사


def f(i, a):
    global maxV
    if a > maxV:
        maxV = a

    visited[i] = 1

    for k in range(1, N+1):
        if adj[i][k] == 1 and visited[k] == 0:
            f(k, a+P[k])


N = int(input())

T = [0]
P = [0]
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# print(T, P)

adj = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if j + T[j] <= N+1:
            if j >= i + T[i]:
                adj[i][j] = 1
# print(adj)

maxV = 0
for i in range(1, N+1):
    if i + T[i] <= N+1:
        # print(i)
        add = P[i]
        visited = [0]*(N+1)
        f(i, add)
print(maxV)
