import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 비용 계산
def calc(choose):
    temp = choose[:]
    temp.append(choose[0])
    cost = 0
    for i in range(n):
        start = temp[i]
        end = temp[i+1]
        # 연결 안되어 있음
        if not board[start][end]:
            return float('inf')
        cost += board[start][end]
    return cost

# backtracking
choose = []
mn = float('inf')
def choice(num):
    global mn
    if num == n:
        mn = min(mn, calc(choose))
        return

    for i in range(n):
        if i not in choose:
            choose.append(i)
            choice(num + 1)
            choose.pop()

# main
choice(0)
print(mn)