n = int(input())
nums = list(map(int, input().split()))

ans = float('inf')

def calc():
    cal_1 = 0
    cal_2 = 0

    for i in range(2 * n):
        if i in choice:
            cal_1 += nums[i]
        else:
            cal_2 += nums[i]

    return abs(cal_1 - cal_2)

choice = []
def choose(idx, num):
    global ans
    if num == n:
        ans = min(ans, calc())
        return

    for i in range(idx, 2 * n):
        # 인덱스가 아닌 값(nums[i])으로 넘기면 같은 값이 여러번 nums 에 있을 때 calc()에서 오류 나기 쉬움
        choice.append(i)
        choose(i + 1, num + 1)
        choice.pop()

choose(0, 0)
print(ans)

'''
2
1 1 2 4

2
'''

'''
# sol_2 - visited 사용 
n = int(input())
num = list(map(int, input().split()))
visited = [False for _ in range(2 * n)]

ans = INT_MAX


def calc():
    diff = 0
    for i in range(2 * n):
        diff = (diff + num[i]) if visited[i] else diff - num[i]
    
    return abs(diff)


def find_min(idx, cnt):
    global ans
    
    if cnt == n:
        ans = min(ans, calc())
        return
    
    if idx == 2 * n:
        return
    
    # 현재 숫자를 첫 번째 그룹에 사용한 경우입니다.
    visited[idx] = True
    find_min(idx + 1, cnt + 1)
    visited[idx] = False
    
    # 현재 숫자를 두 번째 그룹에 사용한 경우입니다.
    find_min(idx + 1, cnt)
    

find_min(0, 0)
print(ans)
'''