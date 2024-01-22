import sys
input= sys.stdin.readline

n = int(input())
meeting = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

meeting.sort(key = lambda x:(x[1], x[0]))

cnt = 1
end_time = meeting[0][1]
for i in range(1, n):
    if end_time <= meeting[i][0]:
        end_time = meeting[i][1]
        cnt += 1

print(cnt)