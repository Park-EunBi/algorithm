def solution(array, commands):
    # 인덱스 값이기에 -1 해주는 거 잊지 말기
    result = []
    for c in range(len(commands)):
        copy_array = array
        i, j, k = commands[c][0]-1, commands[c][1], commands[c][2]-1
        copy_array = copy_array[i:j]
        copy_array.sort()
        result.append(copy_array[k])
    return result

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))