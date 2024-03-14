t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    start = 0
    count = 0

    for j in range(n):
        while True:

            if start == m or a[j] <= b[start]:
                count += start
                break
            else:
                start += 1

    print(count)