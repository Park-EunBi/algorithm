n, m = map(int, input().split())
num = list(map(int, input().split()))

nlst = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            three = num[i] + num[j] + num[k]
            if three > m:
                continue
            else:
                nlst.append(three)
print(max(nlst))

# 다른 풀이
'''
from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

permutationArray = permutations(num, 3)
ans = 0
for i in permutationArray:
    if (m + 1 > sum(i)):
        ans = max(ans, sum(i))

print(ans)
'''