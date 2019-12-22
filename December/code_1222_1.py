# 백준 15683번 - 감시

N, K = map(int, input().split())

q = [0]*100001
visited = [0]*100001
start = -1
end = -1

end += 1
q[end] = N
visited[N] = 1

result = 0
while start != end:
    start += 1
    i = q[start]
    if i == K:
        result = visited[i]-1
        break
    for ni in [i+1, i-1, i*2]:
        if 0 <= ni <= 100000 and visited[ni] == 0:
            end += 1
            q[end] = ni
            visited[ni] = visited[i] + 1
print(result)