t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split(' '))
    a = n % h
    b = n // h + 1
    # 주의 - a == 0이면 오류 발생
    if a == 0:
        b -= 1
        a = h
    print(a*100+b)

    # print("{0}{1:02d}".format(a, b), end='')