import sys
input = sys.stdin.readline

n, m = map(int, input().split())
people = {}
ret = []
for _ in range(n):
    people[input().rstrip()] = 1

for _ in range(m):
    name = input().rstrip()
    if name in people:
        ret.append(name)

ret.sort()
print(len(ret))
for r in ret:
    print(r)