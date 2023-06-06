# 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록
# 동일한 위치에 여러 개의 집 존재 가능
# n: 집의 수

n = int(input())
house = list(map(int, input().split()))

house.sort()
minus = house[(n -1)//2]
print(minus)

'''
<testCase>
4
5 1 7 9

<answer>
5
'''