# m: 평론가, n: 소시지
# 평론가들이 같은 양을 받게 소시지 자르기
# 소시지를 자르는 횟수를 최소로하기

n, m = map(int, input().split())

def gcd(x, y):
    if x < y:
        x, y = y, x

    while 1:
        if y == 0:
            break
        x, y = y, x % y
    return x


print(m-gcd(n, m))