n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    ans.append(cnt)

print(*ans)