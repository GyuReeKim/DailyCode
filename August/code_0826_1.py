T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = list(map(int, input().split()))
    
    # day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # day = 0
    # result = 0
    # if m1 == m2:
    #     result = d2 - d1 + 1
    # else:
    #     for m in range(m1-1, m2-1):
    #         day += day_list[m]
    #         result = day + d2 -d1 + 1
    # print(f'#{tc} {result}')

    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m2 - m1 == 0:
        print(f'#{tc} {d2 - d1 + 1}')
    else:
        day_sum = sum(day_list[m1-1: m2-1])
        print(f'#{tc} {day_sum + d2 - d1  + 1}')