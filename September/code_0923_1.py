# 최소 생산 비용 변형문제

def perm(n, k):
    global minV
    if n == k:
        s = 0
        for i in range(N):
            s += (abs(local[i][0]-factory[p[i]][0]) + abs(local[i][1]-factory[p[i]][1]))
        print(s)
        if s < minV:
            minV = s
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]


# N = 3
N = int(input())
# local = [[-24, -3], [-59, 5], [-2, -79]]
local = [list(map(int, input().split())) for _ in range(N)]
# factory = [[25, -15], [-15, 71], [-99, -92]]
factory = [list(map(int, input().split())) for _ in range(N)]
p = [_ for _ in range(N)]
minV = 1000000
perm(0, N)
print(minV)