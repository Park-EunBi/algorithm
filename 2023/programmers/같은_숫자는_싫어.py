def solution(arr):
    # 리스트에 값넣기
    res = []
    for i in range(len(arr)):
        if i == 0:
            res.append(arr[i])
        elif arr[i] != arr[i - 1]:
            res.append(arr[i])
    return res

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))