import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

# print(23 * 60 * 60) # 82800 => 모두 확인 가능
# 00시 00분 00초 ~ 23시 59분 59초

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
