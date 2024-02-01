import sys
k, p, n = map(int, input().split())
m = 1000000007
ret = k
for _ in range(n):
    a = ret % m
    b = p % m
    ret = (a * b) % m

print(ret)

'''
# 시간 초과 
import sys
k, p, n = map(int, input().split())
print((k * (p ** n)) % 1000000007) # 거듭제곱 연산 때문
'''