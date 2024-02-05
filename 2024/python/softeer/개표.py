import sys

n = int(input())
for _ in range(n):
    num = int(input())
    five = num // 5
    rest = num % 5
    string = '++++ ' * five + '|' * rest
    if rest == 0:
        print(string[:-1])
    else:
        print(string)

