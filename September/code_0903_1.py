T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(len(num), 0, -1):
        for j in range(i-1):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    # print(num)

    maxC = 0
    cnt = 1
    n = 0
    for i in range(1, len(num)):
        if i == len(num)-1 or num[i] != num[i-1]:
            if cnt >= maxC:
                maxC = cnt
                n = num[i-1]
                cnt = 1
            else:
                cnt = 1
        else:
            cnt += 1
    print('#{} {}'.format(tc, n))