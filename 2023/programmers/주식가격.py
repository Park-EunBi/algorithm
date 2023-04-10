def solution(prices):
    result = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i, len(prices) - 1): # 범위 설정 잘 하기
            if prices[i] <= prices[j]:
                result[i] += 1
            else:
                break
    return result

print(solution([1, 2, 3, 2, 3]))


