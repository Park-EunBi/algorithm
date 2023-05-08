# 다양한 수로 이루어진 배열 중
# 주어진 수를 m 번 더하여 가장 큰 수를 만드는 법칙
# 특정 인텍스가 연속해서 k 번 반복될 수 없음

# 2, 4, 5, 4, 6 , m : 8, k : 3
# 6 6 6 5 6 6 6 5
# 인덱스가 다르면 다른 숫자로 취급

'''
<testcase>
5 8 3
2 4 5 4 6
<answer>
46
'''

n, m, k = map(int, input().split())
nums = []

nums = list(map(int, input().split()))
nums.sort(reverse=True)

result = 0
cnt = 0

# m 번 반복하면서
for _ in range(m):
    # 몇번째 같은 수를 더하고 있는지 체크
    if cnt < k:
        result += nums[0]
        cnt += 1
    # k 만큼 반복했다면
    # 두번째로 큰 수 더하기
    else:
        result += nums[1]
        cnt = 0

print(result)

