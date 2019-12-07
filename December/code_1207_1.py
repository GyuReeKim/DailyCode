# 백준 15649번 - N과 M (1)

# p = [[1, 2, 3, 4], [1, 2, 4, 3], [2, 1, 3, 4], [3, 4, 1, 2]]

# # p = sorted(p, key = lambda x: (x[1], x[0]))
# # p = sorted(p, key = lambda x: x[3])
# # print(p)
# # p = sorted(p, key = lambda x: x[2])
# # print(p)
# # p = sorted(p, key = lambda x: x[1])
# # print(p)
# # p = sorted(p, key = lambda x: x[0])
# # print(p)

# for k in range(4):
#     p = sorted(p, key = lambda x: x[4-1-k])
#     print(p)


def perm(n, k, m):
    global p_list
    if n == m:
        p_list.append(p[:m])
    else:
        for i in range(n, k):
            p[i], p[n] = p[n], p[i]
            perm(n+1, k, m)
            p[i], p[n] = p[n], p[i]


N, M = map(int, input().split())

p = [str(i+1) for i in range(N)]
# print(p)
p_list = []

perm(0, N, M)
# print(p_list)

for k in range(M):
    p_list = sorted(p_list, key = lambda x: x[M-1-k])
# print(p_list)

for k in range(len(p_list)):
    print(' '.join(p_list[k]))