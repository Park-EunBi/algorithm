# N개의 자연수 중에서 M개를 고른 수열
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [0 for _ in range(n)]
choose = []
def choice(num):
    if num == m:
        print(' '.join(map(str, choose)))
        return

    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != nums[i]: # in 연산자 사용하면 시간 초과 위험
            choose.append(nums[i])
            visited[i] = 1
            overlap = nums[i]
            choice(num + 1)
            choose.pop()
            visited[i] = 0


choice(0)