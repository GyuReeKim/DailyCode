# 백준 15650번 - N과 M (2)

N, M = map(int, input().split())

p = [str(i+1) for i in range(N)]

p_list = []
for i in range(1, 1<<N):
    temp = []
    for j in range(N):
        if i & (1<<j):
            temp.append(p[j])
    # print(temp)

    if len(temp) == M:
        p_list.append(temp)
# print(p_list)

for k in range(M):
    p_list = sorted(p_list, key = lambda x: x[M-1-k])

for k in range(len(p_list)):
    print(' '.join(p_list[k]))