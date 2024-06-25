def solution(X, Y):
    x = [0 for _ in range(10)]
    y = [0 for _ in range(10)]

    ans = ''

    for num in X:
        x[int(num)] += 1

    for num in Y:
        y[int(num)] += 1

    for i in range(9, -1, -1):
        ans += str(i) * (min(x[i], y[i]))

    '''
    sol2)
    idx = 0
    for num1, num2 in zip(x, y):

        if abs(num1 - num2) >= 0 and num1 != 0 and num2 != 0:
            ans += str(idx) * (min(num1, num2))

        idx += 1

    ans = ans[::-1]
    '''

    if not len(ans):
        ans = '-1'
    elif len(ans) and ans[0] == '0':
        ans = '0'

    return ans