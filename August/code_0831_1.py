T = int(input())
for tc in range(1, T+1):
    num = int(input())
    
    a = 0
    while num % 2 == 0:
        num = num // 2
        a += 1
    # print(a)

    b = 0
    while num % 3 == 0:
        num = num // 3
        b += 1
    # print(b)

    c = 0
    while num % 5 == 0:
        num = num // 5
        c += 1
    # print(c)

    d = 0
    while num % 7 == 0:
        num = num // 7
        d += 1
    # print(d)

    e = 0
    while num % 11 == 0:
        num = num // 11
        e += 1
    # print(e)

    print(f'#{tc} {a} {b} {c} {d} {e}')