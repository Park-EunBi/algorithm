# 숫자 사이에 x, + 연산자를 넣어 가장 큰 수를 만들자
# 모든 연산은 왼쪽 부터 순서대로 (+ 먼저오면 먼저 연산)

num = list(map(int, input()))
num.sort(reverse=True)

# result 의 초기 값을 1으로 설정하면 000이 들어왔을 때 오답
result = num[0]
for i in range(1, len(num)):
    n = num[i]
    # 0, 1 일 경우 더하기
    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

print(result)

'''
<testCase>
02984
<answer>
576

<testCase>
567
<answer>
210
'''