# 주말.md 문제1
N = 10
numbers = [7, 2, 3, 4, 1, 2, 5, 4, 5, 6]

count = 0
high = []
# length = []
for number in range(2, N):
    if numbers[number-2] - numbers[number-1] < 0:
        if numbers[number-1] - numbers[number] > 0:
            count += 1
            high.append(number)
print(count)
print(high)