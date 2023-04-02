n = input()

res = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    # 0을 곱하면 안되기에 res <= 1이라는 조건도 있음 
    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num
print(res)

'''
# 잘못된 풀이 
# 1이 올 경우 더하는 것이 더 좋다 
# 무조건 다 더하려고 함 
# 그리고 0이 중간에 올 수도 있음 
n = int(input())
res = 1
while n >0:
    res *= (n% 10)
    n //= 10
print(res)
'''
