n = int(input())
m = int(input())
string = input()

# 투 포인터
left, right = 0, 0
ans = 0

while right < m:
    if string[right:right + 3] == 'IOI': # 3개씩 슬라이싱
        right += 2
        if right - left == 2 * n: # IOI 몇 개인지 확인
            ans += 1
            left += 2 # 세어야 하는 IOI 개수가 맞을 때 left 이동
    else:
        left = right = right + 1

print(ans)
