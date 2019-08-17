# 주말.md 문제4
# import pprint


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
# arr = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 1], [1, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1]]
# arr[i-1][j] # 상
# arr[i+1][j] # 하
# arr[i][j-1] # 좌
# arr[i][j+1] # 우

count = 0
for i in range(1, N-1): # 열
    for j in range(1, N-1): # 행
        if arr[i][j] == 1:
            if arr[i-1][j] == 0 and arr[i+1][j] == 0 and arr[i][j-1] == 0 and arr[i][j+1] == 0:
                count += 1

# pprint.pprint(arr, indent=3, width=50)
print(count)