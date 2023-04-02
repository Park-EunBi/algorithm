# 파이썬의 특징을 반영한 퀵소트
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트

    # 오른쪽 분할
    left_side = [x for x in tail if x <= pivot]
    # 왼쪽 분할
    right_side = [x for x in tail if x > pivot]

    # 각각 분할 수 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))