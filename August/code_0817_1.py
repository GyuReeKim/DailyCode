# 주말.md 문제1

# N = [4, 5, 1, 2, 3, 2, 1]

N = list(map(int, input().split()))

count_list = []
count = 0
for n in range(1, len(N)-1):
    if N[n-1] - N[n] == 1:
        count += 1
        if N[n] - N[n+1] == 1:
            if n == len(N)-2:
                count += 1
                count_list.append(count)
            else:
                count += 1
        elif N[n] - N[n+1] == -1:
            count_list.append(count)
            count = 1
        else:
            count_list.append(count)
            count = 0
    if N[n-1] - N[n] == -1:
        count += 1
        if N[n] - N[n+1] == -1:
            if n == len(N)-2:
                count += 1
                count_list.append(count)
            else:
                count += 1
        elif N[n] - N[n+1] == 1:
            count_list.append(count)
            count = 1
        else:
            count_list.append(count)
            count = 0
# print(count_list)

count_max = 0
for c in count_list:
    if c > count_max:
        count_max = c
print(count_max)