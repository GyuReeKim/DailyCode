T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = list(map(int, input().split()))
    
    month = m2 - m1
    day = d2 - d1
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 0:
        print(f'#{tc} {day+1}')
    else:
        if m2 > m1:
            if d2 > d1:
                day_sum = sum(day_list[m1-1: m2-1])
                print(f'#{tc} {day_sum + day + 1}')
            else:
                day_sum = sum(day_list[m1: m2-1])
                print(day_list[m1-1]-d1+1)
                print(f'#{tc} {day_sum + day_list[m1-1] -d1 + 1 + d2}')


