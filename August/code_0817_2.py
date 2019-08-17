# 주말.md 문제2

N = int(input())
numbers = list(map(int, input().split()))

# 1번
count = 0
high = []
for number in range(1, N-1):
    if numbers[number-1] - numbers[number] < 0:
        if numbers[number] - numbers[number+1] > 0:
            count += 1
            high.append(number)
print(count)
# print(high)

# 2번
length = []
for n in range(N):
    if len(high) == 1:
        print(0)
    else:
        if high[0] <= n < high[-1]:
            l = numbers[n] - numbers[n+1]
            if l < 0:
                l = -l
            length.append(l)
# print(length)

max_length = 0
for i in length:
    if i > max_length:
        max_length = i
print(max_length)