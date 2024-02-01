import sys
n = int(input())
dot = 2
for i in range(1, n + 1):
    dot += (2**(i-1))

print(dot*dot)