nums = [list(map(int, input().split())) for _ in range(int(input()))]
nums.sort(key = lambda x: (x[0], x[1]))
print('\n'.join([' '.join(map(str, num)) for num in nums]))