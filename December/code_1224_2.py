# 백준 14501번 - 퇴사


def f(i, r, s): # i 현재 날짜, r 진행중인 상담의 남은 날짜, s 현재 이익
    # print(i, r, s)
    global maxV
    if i == N:
        if s > maxV:
            maxV = s
    else:
        if r == 0 and T[i]+i <= N:
            f(i+1, T[i]-1, s+P[i])
        if r-1 < 0:
            r = 1
        f(i+1, r-1, s)


N = int(input())

T = []
P = []
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

maxV = 0
f(0, 0, 0)
print(maxV)