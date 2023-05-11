# n: 캐릭터의 점수
# 왼쪽 부분의 자릿수의 합과 오른쪽 자리수의 합이 동일한 상황 인지 판단하기

n = list(map(int, input()))
length = int(len(n) / 2)

if sum(n[:length]) == sum(n[length:]):
    print('LUCKY')
else:
    print('READY')

'''
<testCase>
123402
<answer>
LUCKY

<testCase>
7755
<answer>
READY
'''