import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for _ in range(n):
    adr, pwd = input().split()
    dict[adr] = pwd

for _ in range(m):
    print(dict[input().rstrip()])