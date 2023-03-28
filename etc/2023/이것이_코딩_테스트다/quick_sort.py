# quick sort

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    # left 와 right 가 엇갈리면 종료
    while left <= right:
        # 피벗보다 큰 값 찾기
        # 조건에 맞지 않으니 인덱스만 증가
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 값 찾기
        # 조건에 맞지 않으니 인덱스만 감소
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸을 때
            array[right], array[pivot] = array[pivot], array[left]
        else: # 엇갈리지 않았을 때, 작은 값과 큰 값을 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 다시 정렬
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array -1))
print(array)