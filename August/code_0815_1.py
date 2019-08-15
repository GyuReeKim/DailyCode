# Sum
# import pprint
for tc in range(1, 11):
    t = int(input())
    arr = [[0]*100 for a in range(100)]

    for i in range(100):
        A = list(map(int, input().split()))
        for j in range(100):
            arr[i][j] = A[j]
    # pprint.pprint(arr, indent=4, width=1000)

    sum_list = []
    sum1 = 0
    sum2 = 0
    for i in range(100):
        r = 0
        c = 0
        for j in range(100):
            r += arr[i][j]
            c += arr[j][i]
            if i + j == 99:
                sum1 += arr[i][j]
            if i == j:
                sum2 += arr[i][j]
        sum_list.append(r)
        sum_list.append(c)
    sum_list.append(sum1)
    sum_list.append(sum2)

    print('#{} {}'.format(tc, max(sum_list)))