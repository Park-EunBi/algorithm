a, b = map(int, input().split())

mn = min(a, b)

# 최대 공약수
ans = 0
for i in range(mn, 0, -1):
    if a % i == 0 and b % i == 0:
        ans = i
        print(i)
        break

# 최소 공배수
print(ans * (a // ans) * (b // ans))