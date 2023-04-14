def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2) : -idx]:
            return False
    else:
        return True

def recursice(num):
    global N, res
    if len(num) == N:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            recursice(num + str(i))
    return

N = int(input())
recursice('1')

'''
# 메모리 초과
# 임의의 길이의 인접한 두 부분 수열이 있으면 나쁜 수열
from itertools import product

n = int(input())
bad = ['1', '2', '3', '12', '13', '23', '123']

# n번의 반복으로 만들 수 있는 수열
nums = product(['1', '2', '3'], repeat= n )
nums_list = [''.join(x) for x in nums]

for n in nums_list:
    for b in bad:
        if b*2 in n:
            break
    else:
        print(n, end='')
        break
'''

