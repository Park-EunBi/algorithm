# 숫자로 이루어진 문자열 s
# 'x', '+' 연산자를 넣어 가장 큰 수를 구하는 프로그램

n = list(map(int, input()))

n.sort(reverse=True)
ret = 1

for i in n:
    if i == 0 or i == 1:
        ret += i
    else:
        ret *= i

print(ret)