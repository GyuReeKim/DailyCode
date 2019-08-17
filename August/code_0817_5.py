# 주말.md 문제5
import pprint

# N = int(input())
# arr = [list(map(int, input().split())) for n in range(N)]
# arr[i-1][j] # 상
# arr[i+1][j] # 하
# arr[i][j-1] # 좌
# arr[i][j+1] # 우
# arr[i-1][j-1] # 좌상
# arr[i-1][j+1] # 우상
# arr[i+1][j-1] # 좌하
# arr[i+1][j+1] # 우하

N = 5
arr = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 1, 1], [1, 1, 3, 1, 1], [1, 2, 1, 1, 3]]

count = 0
for i in range(1, N-1):
    for j in range(1, N-1):
        if arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i-1][j-1] and arr[i][j] > arr[i-1][j+1] and arr[i][j] > arr[i+1][j-1] and arr[i][j] > arr[i+1][j+1]:
            count += 1

pprint.pprint(arr, indent=3, width=50)
print(count)
