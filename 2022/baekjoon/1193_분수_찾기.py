n = int(input())

line = 0
max = 0

while n > max:
    line += 1
    max += line

sub = max - n

if line % 2 == 0:
    a = line - sub
    b = sub + 1

else:
    a = sub + 1
    b = line - sub

print('{0}/{1}'.format(a, b))

'''
cnt = 0 # 계차
num = 1 # 계산한 값

while 1:
    if n == 1:
        break
    else:
        cnt += 1
        num += cnt
        if n < num:
            break

if n != 1:
    cnt -= 1
    num -= 1

sub = num - n
if (cnt % 2 != 0):
    a = cnt + 1
    b = 1
    if sub != 0:
        a -= sub
        b += sub
else:
    a = 1
    b = cnt + 1
    if sub != 0:
        a += sub
        b -= sub

print('{0}/{1}'.format(a, b))
'''