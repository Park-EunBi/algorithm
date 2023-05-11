# 알파벳 대문자, 숫자로만 구성된 문자열이 입력
# 모든 알파벳 오름차순 정렬, 이어서 숫자를 더한 값 출력

S = input()
alpha = []
num = []
for s in S:
    if s.isalpha():
        alpha.append(s)
    else:
        num.append(int(s))

alpha.sort()

print(''.join(alpha) + ''+  str(sum(num)))

'''
<testCase>
K1KA5CB7
<answer>
ABCKK13

<testCase>
AJKDLSI412K4JSJ9D
<answer>
ADDIJJKKLSS20
'''