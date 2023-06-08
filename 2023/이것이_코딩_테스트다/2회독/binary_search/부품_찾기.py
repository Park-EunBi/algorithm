# n 개의 부품, m 개 종류의 부품 대량 주문
# 가게 안에 부품이 모두 있는지 확인

def binary_search(start, target, end, array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    else:
        return 'no'

n = int(input())
store = list(map(int, input().split()))
m = int(input())
now = list(map(int, input().split()))

store.sort()

for i in now:
    print(binary_search(0, i, n-1, store), end=' ')

'''
<testCase>
5
8 3 7 9 2
3
5 7 9

<answer>
no yes yes
'''

'''
# 계수 정렬 사용 
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end= ' ')
'''

'''
# set 사용 
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''