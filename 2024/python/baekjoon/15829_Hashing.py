R = 31
M = 1234567891
n = int(input())
word = input()

ret = 0
for i in range(n):
    ret += ((ord(word[i]) - 96) * R ** i)

print(ret % M)