# 당근 수확 4

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input().split())) for _ in range(N)]
    
    s1 = 0
    for i in range(0, N//2):
        for j in range(i+1, N-(i+1)):
            s1 += farm[i][j]

    s2 = 0
    for i in range(1, N-1):
        if i <= N//2:
            for j in range(0, i):
                s2 += farm[i][j]
        else:
            for j in range(0, N-(i+1)):
                s2 += farm[i][j]

    s3 = 0
    for i in range(1, N-1):
        if i <= N//2:
            for j in range(N-i, N):
                s3 += farm[i][j]
        else:
            for j in range(i+1, N):
                s3 += farm[i][j]

    s4 = 0
    for i in range(N//2+1, N):
        for j in range(N-i, i):
            s4 += farm[i][j]

    maxV = max(s1, s2, s3, s4)
    minV = min(s1, s2, s3, s4)

    print('#{} {}'.format(tc, maxV-minV))