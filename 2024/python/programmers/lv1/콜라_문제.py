def solution(a, b, n):
    answer = 0

    while n >= a:
        tmp = n % a
        n = (n // a) * b # n 갱신 필요
        answer += n
        n += tmp

    return answer

'''
# sol2)
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

# sol3)
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer
'''