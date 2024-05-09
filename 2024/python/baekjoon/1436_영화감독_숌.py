n = int(input())
ans = 0
num = 666

while 1:
    if '666' in str(num):
        ans += 1

    if ans == n:
        break

    num += 1

print(num)