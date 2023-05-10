# 8 x 8 좌표 평면
# L 자로만 이동 가능 (수평 2 수직 1 or 수평 1 수직 2)
# 시작 지점이 주어졌을 때 동 경우의 수 출력

# 열을 수로 변환 (1부터 시작)
col_types = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

location = input()
x = col_types.index(location[0])
# 다른 방법 - 교재
# x = int(ord(location[0])) - int(ord('a')) + 1
y = int(location[1])


# 이동 방향 설정
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]
count = 0

for i in range(8):
    # 임시로 이동
    nx = x + dx[i]
    ny = y + dy[i]

    # 위치를 벗어나는지 확인
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    # 가능하면 카운트
    count += 1

print(count)

'''
<testCase>
a1
<answer>
2

<testCase>
a7
<answer>
3

<testCase>
d5
<answer>
8
'''