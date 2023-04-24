# 이진 탐색 - 재귀
def binary_search(array, target, start, end):
    # 역전되었다면 찾는 값이 없는 것
    if start > end :
        return None
    # 비교 대상 선정
    mid = (start + end) //2
    # 찾았다면, 값 리턴
    if array[mid] == target:
        return mid
    # 타깃보다 값이 크면 뒤 쪽 조사
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 타깃보다 값이 작으면 앞 쪽 조사
    else:
        return binary_search(array, target, mid+1, end)

print(binary_search([1, 2, 3, 4, 6, 7, 9], 6, 0, 7))