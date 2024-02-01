import sys
m, n, k = map(int, input().split())
secret = list(map(str, input().split()))
secret = ''.join(secret)
input_num = list(map(str, input().split()))
input_num = ''.join(input_num)

print('secret') if secret in input_num else print('normal')