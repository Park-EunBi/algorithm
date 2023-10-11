# 나이 증가 -> 먼저 가입

n = int(input())

user = []
for _ in range(n):
    age, name = input().split()
    user.append([int(age), name])

user.sort(key= lambda x: x[0])

for u in user:
    print(u[0], u[1])