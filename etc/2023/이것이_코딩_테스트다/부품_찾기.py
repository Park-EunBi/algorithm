import sys
sys.stdin = open("input.txt", "rt")

# 부품 n 개, m 개의 종류를 대량 주문
# 모든 부품이 존재하는지 찾기
# 있으면 yes, 없으면 no

n = int(input())
store = list(map(int, input().split()))
store.sort()
m = int(input())
order = list(map(int, input().split()))
order.sort()

def binary_search(array, target, start, end):
    if start > end :
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)



for o in order:
    # 하나씩 존재하는지 확인하기
    print(binary_search(store, o, 0, n-1), end=' ')

'''
# 다른 풀이 - 계수 정렬 이용 
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''

'''
# 다른 풀이 - set 사용 
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''