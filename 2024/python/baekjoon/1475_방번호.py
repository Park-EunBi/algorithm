n = int(input())
cnt = [0 for _ in range(10)]
for num in str(n):
    if int(num) == 6:
        if cnt[6] > cnt[9]:
            cnt[9] += 1
        else:
            cnt[6] += 1
    elif int(num) == 9:
        if cnt[6] > cnt[9]:
            cnt[9] += 1
        else:
            cnt[6] += 1
    else:
        cnt[int(num)] += 1

print(max(cnt))