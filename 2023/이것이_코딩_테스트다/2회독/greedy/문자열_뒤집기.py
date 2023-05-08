# 0과 1로만 이루어진 문자열 s
# 문자열 s에 있는 모든 숫자를 같게 만듦
# 최소 횟수 구하기

s = list(map(int, input()))
print(s)

zeroCount = 0
oneCount = 0

if s[0] == 1:
    zeroCount += 1
else:
    oneCount += 1

# 모든 원소 확인
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == 1:
            zeroCount += 1
        else:
            oneCount += 1

print(min(zeroCount, oneCount))


'''
<testCase>
0001100
<answer>
1
'''