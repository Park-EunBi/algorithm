d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 계산한 적 있으면
    if d[x] != 0:
        return d[x]
    # 계산하지 않았다면
    # 계산 결과를 리스트에 저장하는 것이 기존 방법과 다르다
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))