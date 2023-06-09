# n 개의 원소를 포함한 수열, 오름차순 정렬
# x 가 등장하는 횟수 계산 (없으면 -1)
# O(logN)으로 설계

# 이진 탐색
# 0. 등장 횟수 세기
def count_nums(array, x):
    n = len(array)

    first_idx = first(array, x, 0, n-1)

    if first_idx == None:
        return 0

    last_idx = last(array, x, 0, n-1)

    return last_idx - first_idx + 1

# 1. 시작점 찾기
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if(mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid -1)
    else:
        return first(array, target, mid+1, end)

# 2. 끝점 찾기
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n-1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid -1)
    else:
        return last(array, target, mid + 1, end)

n, x = map(int, input().split())
nums = list(map(int, input().split()))

cnt = count_nums(nums, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)

'''
<testCase1>
7 2
1 1 2 2 2 2 3

<answer1>
4

<testCase2>
7 4
1 1 2 2 2 2 3

<answer2>
-1
'''