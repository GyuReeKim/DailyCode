# 스위치
N = int(input())
switch = input().split()
S = int(input())
for s in range(S):
    gender, number = list(map(int, input().split()))

    if gender == 1:
        for i in range(N):
            if (i+1) % number == 0:
                if switch[i] == '0':
                    switch[i] = '1'
                else:
                    switch[i] = '0'
    if gender == 2:
        for i in range(N):
            if (i+1) == number and number <= N//2:
                for j in range(number):
                    if j == 0:
                        if switch[i] == '0':
                            switch[i] = '1'
                        else:
                            switch[i] = '0'
                    else:
                        if switch[i-j] != switch[i+j]:
                            break
                        else:
                            if switch[i+j] == '0':
                                switch[i-j] = '1'
                                switch[i+j] = '1'
                            else:
                                switch[i-j] = '0'
                                switch[i+j] = '0'
            if (i+1) == number and number > N//2:
                for j in range(N - number + 1):
                    if j == 0:
                        if switch[i] == '0':
                            switch[i] = '1'
                        else:
                            switch[i] = '0'
                    else:
                        if switch[i-j] != switch[i+j]:
                            break
                        else:
                            if switch[i+j] == '0':
                                switch[i-j] = '1'
                                switch[i+j] = '1'
                            else:
                                switch[i-j] = '0'
                                switch[i+j] = '0'
# print(switch)
if len(switch) <= 20:
    print(' '.join(switch))
else:
    result = []
    for s in range(len(switch)):
        if s != 0 and s % 20 == 0:
            print(' '.join(result))
            result = []
            result.append(switch[s])
        else:
            result.append(switch[s])
    print(' '.join(result))
