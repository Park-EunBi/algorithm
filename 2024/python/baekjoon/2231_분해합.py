n = int(input())
num = n//2
while 1:

    ret = num
    for s in str(num):
        ret += int(s)

    if ret == n:
        print(num)
        break

    # 생성자가 없을 경우 시간 초과 가능
    if num == n:
        print(0)
        break

    num += 1