import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    order = list(input().split())
    if order[0] == 'push':
        stack.append(int(order[1]))

    elif order[0] == 'pop':
        print(-1) if not len(stack) else print(stack.pop(-1))

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        print(1) if not len(stack) else print(0)

    elif order[0] == 'top':
        print(-1) if not len(stack) else print(stack[-1])