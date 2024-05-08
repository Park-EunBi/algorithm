import sys
input = sys.stdin.readline

n = int(input())
deque = []
for _ in range(n):
    commend = list(input().split())
    if commend[0] == 'push_front':
        deque.insert(0, commend[1])
    elif commend[0] == 'push_back':
        deque.append(commend[1])
    elif commend[0] == 'pop_front':
        if deque:
            print(deque[0])
            deque = deque[1:]
        else:
            print(-1)
    elif commend[0] =='pop_back':
        if deque:
            print(deque[-1])
            deque = deque[:-1]
        else:
            print(-1)
    elif commend[0] == 'size':
        print(len(deque))
    elif commend[0] == 'empty':
        if len(deque):
            print(0)
        else:
            print(1)
    elif commend[0] == 'front':
        if len(deque):
            print(deque[0])
        else:
            print(-1)
    elif commend[0] == 'back':
        if len(deque):
            print(deque[-1])
        else:
            print(-1)