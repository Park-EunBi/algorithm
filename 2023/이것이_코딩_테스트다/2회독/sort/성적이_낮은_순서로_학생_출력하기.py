# 성적이 낮은 순서로 출력
n = int(input())
scores = []
for _ in range(n):
    scores.append(input().split(' '))

scores.sort(key=lambda x: int(x[1]))

for s in scores:
    print(s[0], end=' ')

'''
<testCase>
2
홍길동 95
이순신 77

<answer>
이순신 홍길동
'''