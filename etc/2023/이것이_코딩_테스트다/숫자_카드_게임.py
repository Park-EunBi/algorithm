import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

mins = []
for _ in range(n):
    mins.append(min(list(map(int, input().split()))))
print(max(mins))

