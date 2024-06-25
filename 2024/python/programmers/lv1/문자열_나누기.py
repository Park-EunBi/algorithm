def solution(s):
    cnt = [0, 0]  # x, 다른 글자 등장 횟수
    x = s[0]
    ans = 0

    for idx, char in enumerate(s):
        if char == x:
            cnt[0] += 1
        else:
            cnt[1] += 1

        # 등장 횟수가 같으면 분리
        if cnt[0] == cnt[1]:
            ans += 1
            cnt = [0, 0] # 등장 횟수 초기화

            # 인덱스 에러 방지
            if idx != len(s) - 1:
                x = s[idx + 1]

    # 딱 나누어 떨어지지 않을 때
    if cnt[0] != cnt[1]:
        ans += 1

    return ans

'''
from collections import deque

def solution(s):

    ans = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans
'''