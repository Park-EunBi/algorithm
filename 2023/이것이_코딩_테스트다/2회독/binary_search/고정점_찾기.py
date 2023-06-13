# p. 368
# 고정점 - 인덱스와 값이 동일한 원소
# 오름차순 정렬되어 있음
# 고정점 출력 (최대 1개 존재, 없으면 -1)
# O(logN)으로 설계

def binary_search(array, start, end):

    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid -1)
    else:
        return binary_search(array, mid + 1, end)


n = int(input())
nums = list(map(int, input().split()))

idx = binary_search(nums, 0, n-1)

if idx == None:
    print(-1)
else:
    print(idx)


'''
<testCase1>
5
-15 -6 1 3 7

<answer1>
3

<testCase2>
7
-15 -4 2 8 9 13 15

<answer2>
2

<testCase3>
7
-15 -4 3 8 9 13 15

<answer3>
-1

'''