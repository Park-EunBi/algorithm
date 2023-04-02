import sys

n = int(sys.stdin.readline())
strs= []

for i in range(n):
    strs.append(sys.stdin.readline().strip())

'''
런타임 에러
n = int(input())
strs = []
for _ in range(n):
    strs.append(input())
'''
strs = set(strs)
strs = list(strs)

strs.sort()
strs = sorted(key= len)
# strs = sorted(set(strs), key= len)

for s in strs:
    print(s)


