import math
a, b, v = map(int, input().split(' '))

day = math.ceil((v - b) / (a - b)) 
# 아침에 정상에 도달한 것을 반영한 식 
# 내림이 아닌 올림을 해야 함
print(day)


'''
day = int(v / (a - b))
if v <= ((a - b) * (day - 1)) + b: # 낮에 정상에 도달했다면 
    day -= 1
else:
    day += 1

print(day)
'''

'''
시간 초과
height = 0
cnt = 0
while 1:
    height += a
    cnt += 1
    if height >= v:
        break
    height -= b
    if height >= v:
        break
'''
