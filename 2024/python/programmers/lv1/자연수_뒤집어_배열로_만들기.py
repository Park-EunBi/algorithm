def solution(n):
    ret = []
    for i in str(n):
        ret.insert(0, int(i))
    return ret