n, m = map(int, input().split())

choose = []
def choice(num):
    if num == m:
        print(*choose)
        return

    for i in range(1, n+1):
        choose.append(i)
        choice(num + 1)
        choose.pop()

choice(0)