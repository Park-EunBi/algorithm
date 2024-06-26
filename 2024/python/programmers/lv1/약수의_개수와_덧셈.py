def solution(left, right):
    cnt = [1 for _ in range(1002)]
    for i in range(1, 1002): # 시간 복잡도 O(nlogn)
        for j in range(i * 2, 1002, i):
            cnt[j] += 1

    ans = 0
    for i in range(left, right + 1):
        if cnt[i] % 2:
            ans -= i
        else:
            ans += i

    return ans