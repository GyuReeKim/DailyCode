# 백준 15686번 - 치킨 배달

def f(n, m, k, l):
    global minV
    if n == l:
        # print(chicken)
        street = 0
        for h in range(len(home)):
            minH = 1000000
            for r in range(l):
                length = abs(home[h][0] - chicken[r][0]) + abs(home[h][1] - chicken[r][1])
                if length < minH:
                    minH = length
            # print(minH)
            street += minH
        # print(street)
        if street < minV:
            minV = street
    else:
        for i in range(m, k-(l-n)+1):
            chicken[n] = stores[i]
            f(n+1, i+1, k, l)


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

k = 0
stores = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            k += 1
            stores.append((i, j))
        elif city[i][j] == 1:
            home.append((i, j))
# print(stores)
chicken = [0]*M
minV = 1000000
f(0, 0, k, M)
print(minV)