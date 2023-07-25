# +, -, *, / 연산자를 하나씩 넣어 수식을 만들기
# 주어진 수의 순서는 바꿀 수 없다. 식의 계산은 무조건 앞에서부터 진행

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최대, 최솟값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산 수행 (재귀)
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now/data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)

'''
<testCase1>
2
5 6
0 0 1 0

<answer1>
30
30

<testCase2>
3
3 4 5
1 0 1 0

<answer2>
35
17
'''