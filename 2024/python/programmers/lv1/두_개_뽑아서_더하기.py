def solution(numbers):
    ans = set()
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            ans.add(numbers[i] + numbers[j])

    return sorted(list(ans))