# 0/1 Knapsack
# 시간초과

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    V = []
    C = []
    for i in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)
    # print(V, C)

    maxC = 0
    for i in range(1<<N):
        temp = 0
        cnt = 0
        for j in range(N):
            if i & (1<<j):
                temp += V[j]
                cnt += C[j]
                if temp > K:
                    break
        if temp <= K:
            if cnt > maxC:
                maxC = cnt
    print('#{} {}'.format(tc, maxC))