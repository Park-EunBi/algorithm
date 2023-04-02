n = int(input())

for _ in range(n):
    r, s = input().split()
    r = int(r)

    for i in range(len(s)):
        for j in range(r):
            print(s[i], end='')

    print()

