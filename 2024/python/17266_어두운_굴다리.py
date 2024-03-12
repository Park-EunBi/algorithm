n, m = int(input()), int(input())
li = [0] + list(map(int, input().split())) + [n]
s, e = 0, n
res = 0

def search(li, m):
    if li[1]-li[0] > m:
        return 0
    if li[-1]-li[-2] > m:
        return 0
    for i in range(1, len(li)-2):
        if (li[i+1]-li[i])/2 > m:
            return 0
    return 1


while s <= e:
    m = (s+e)//2
    if search(li, m):
        e = m-1
        res = m
    else:
        s = m+1

print(res)