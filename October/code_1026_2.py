# 당근밭 옆 고구마밭
# 풀이중

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = list(map(int, input().split()))
    # print(farm)

    cnt = []
    length = 1
    for i in range(1, N):
        if i == N-1:
            if farm[i-1] < farm[i]:
                length += 1
                cnt.append(length)
            else:
                cnt.append(length)
                length = 1
                cnt.append(length)
        else:
            if farm[i-1] < farm[i]:
                length += 1
            else:
                cnt.append(length)
                length = 1
    # print(cnt)

    long = 0
    for i in range(len(cnt)):
        if cnt[i] > 1:
            long += 1
    # print(long)

    length = 1
    add = farm[0]
    maxV = 0
    for i in range(1, N):
        if i == N-1:
            if farm[i-1] < farm[i]:
                length += 1
                add += farm[i]
                if length == max(cnt):
                    if add > maxV:
                        maxV = add
            else:
                if length == max(cnt):
                    if add > maxV:
                        maxV = add
                length = 1
                add = farm[i]
                if length == max(cnt):
                    if add > maxV:
                        maxV = add
        else:
            if farm[i-1] < farm[i]:
                length += 1
                add += farm[i]
            else:
                if length == max(cnt):
                    if add > maxV:
                        maxV = add
                length = 1
                add = farm[i]
    print('#{} {} {}'.format(tc, long, maxV))