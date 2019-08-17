# 주말.md 문제3

N = int(input())
arr = [list(map(int, input().split())) for a in range(N)]
# print(arr)

count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] % 2 == 0:
            count += 1
print(count)