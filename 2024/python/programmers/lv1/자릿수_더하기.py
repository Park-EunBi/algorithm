def solution(n):
    ret = 0
    for s in str(n):
        ret += int(s)
    return ret