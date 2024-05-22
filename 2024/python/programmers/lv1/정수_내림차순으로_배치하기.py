def solution(n):
    ret = [i for i in str(n)]
    ret.sort(reverse = True)
    ret = ''.join(ret)
    return int(ret)