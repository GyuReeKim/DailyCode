# 다시 풀어보기
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) 
    v = list(map(int, input().split()))
    r_list = []
    for n in range(N-M, N):
        v_list = v[n-M+1: n+1]
        v_sum = 0
        for v_l in v_list:
            v_sum += v_l
        r_list.append(v_sum)
    # print(r_list)

    for r in range(M-1, 0, -1):
        for i in range(0, r):
            if r_list[i] > r_list[i+1]:
                temp = r_list[i]
                r_list[i] = r_list[i+1]
                r_list[i+1] = temp
    # print(r_list)
    r_min = r_list[0]
    r_max = r_list[-1]

    print(tc, r_max - r_min)