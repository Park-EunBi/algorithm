def solution(s):
    ans = True

    p = 0
    y = 0

    for st in s:
        if st == 'P' or st == 'p':
            p += 1
        elif st == 'Y' or st == 'y':
            y += 1

    if p != y:
        ans = False

    return ans