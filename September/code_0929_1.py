# [S/W 문제해결 기본] 9일차 - 사칙연산


def postorder(n):
    global result
    if n > 0:
        postorder(ch1[n])
        postorder(ch2[n])
        # print(n, end=' ')
        if par[n] == '+':
            result.append(result.pop(-2) + result.pop(-1))
        elif par[n] == '-':
            result.append(result.pop(-2) - result.pop(-1))
        elif par[n] == '*':
            result.append(result.pop(-2) * result.pop(-1))
        elif par[n] == '/':
            result.append(result.pop(-2) / result.pop(-1))
        else:
            result.append(par[n])


T = 10
for tc in range(1, T+1):
    N = int(input())
    par = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for i in range(N):
        num = input().split()
        if len(num) == 4:
            par[int(num[0])] = num[1]
            ch1[int(num[0])] = int(num[2])
            ch2[int(num[0])] = int(num[3])
        elif len(num) == 3:
            par[int(num[0])] = int(num[1])
            ch1[int(num[0])] = int(num[2])
        else:
            par[int(num[0])] = int(num[1])

    # print(par)
    # print(ch1)
    # print(ch2)
    result = []
    postorder(1)
    print('#{} {}'.format(tc, int(result[0])))