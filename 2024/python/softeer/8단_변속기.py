import sys
nums = list(map(str, input().split()))

asc = '12345678'
desc = '87654321'

num = ''.join(nums)

if num == asc:
    print('ascending')
elif num == desc:
    print('descending')
else:
    print('mixed')