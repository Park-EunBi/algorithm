def solution(n):
    ret = 0
    for i in range(1, n + 1):
        if n % i == 0:
           ret += i
    return ret