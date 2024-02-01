import sys

nums = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1110010',
    '8': '1111111',
    '9': '1111011',
    ' ': '0000000'
}

n = int(input())
for _ in range(n):
    ret = 0
    a, b = map(str, input().split())

    a_zero, b_zero = 5 - len(a), 5 - len(b)
    a = ' ' * a_zero + a  # 빈공간 채우기
    b = ' ' * b_zero + b  # 빈공간 채우기

    for i in range(5):
        for j in range(7):
            if nums[a[i]][j] != nums[b[i]][j]:
                ret += 1
    print(ret)