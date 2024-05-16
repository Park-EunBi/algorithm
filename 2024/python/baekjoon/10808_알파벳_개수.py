cnt = [0 for _ in range(26)]
for s in input():
    cnt[ord(s)-97] += 1

print(*cnt)