def solution(s):
    words = s.split(' ')
    ans = ''

    for w in words:
        if len(w):
            w = w[0].upper() + w[1:].lower()

        ans += (w + ' ')

    return ans[:-1]