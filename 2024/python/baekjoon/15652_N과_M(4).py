n, m = map(int, input().split())

choose = []
def choice(num, before):
    if num == m:
        print(*choose)
        return

    for i in range(before, n + 1):
        choose.append(i)
        choice(num+1, i)
        choose.pop()

choice(0, 1)