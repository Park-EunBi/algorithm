import sys
input = sys.stdin.readline

n = int(input())

li = set()
for _ in range(n):
    commend = list(input().split())
    if commend[0] == 'all':
        li = {i for i in range(1, 21)}

    elif commend[0] == 'empty':
        li = set()

    else:
        com, num = commend[0], int(commend[1])

        if com == 'add':
            li.add(num)

        elif com == 'remove':
            if num in li:
                li.remove(num)

        elif com == 'check':
            print(1) if num in li else print(0)

        elif com == 'toggle':
            li.remove(num) if num in li else li.add(num)