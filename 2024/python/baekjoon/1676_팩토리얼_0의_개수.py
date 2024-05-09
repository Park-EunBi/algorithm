import math
f = str(math.factorial(int(input())))

cnt = 0
for i in range(len(f)-1, -1, -1):
    if f[i] == '0':
        cnt += 1
    else:
        break

print(cnt)