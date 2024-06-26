def solution(food):
    ans = ''
    for i in range(1, len(food)):
        ans += str(i) * (food[i] // 2)

    return ans + '0' + ans[::-1]

    # tmp = ans[::-1]
    # ans += '0'
    # ans += tmp

    # return ans