# 마이너스를 만날 때 가장 큰 수를 빼기
arr = input().split('-')

ans = 0
for i in arr[0].split('+'):
    ans += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)