def solution(sizes):
    for s in sizes:
        s.sort()
    sizes.sort(key=lambda x: (x[0], x[1]))

    mx1, mx2 = 0, 0
    for s in sizes:
        mx1 = max(mx1, s[0])
        mx2 = max(mx2, s[1])

    return mx1 * mx2