s = input().split(' ')
cnt = len(s)

if (s[0] == ''):
    cnt -= 1
if (s[len(s) - 1] == ''):
    cnt -= 1

print(cnt)

