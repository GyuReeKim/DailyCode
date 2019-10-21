# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    last = max(customer)
    bake = [0]*(last+1)
    guest = [0]*(last+1)
    for i in range(N):
        for j in range(last+1):
            if customer[i] == j:
                guest[j] += 1
    result = "Possible"
    for i in range(last+1):
        bake[i] += bake[i-1]
        if i != 0 and i % M == 0:
            bake[i] += K
        # print(bake, guest)
        # print(bake[i], guest[i])
        if bake[i] < guest[i]:
            result = "Impossible"
            break
        bake[i] -= guest[i]
    print('#{} {}'.format(tc, result))
