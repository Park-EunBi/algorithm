# n: 볼링공의 개수, m: 볼링공의 최대 무게 (같은 무게여도 다른 공)
# 고를 수 있는 볼링공 번호의 경우의 수 출력 (같은 무게 고를 수 없음)

n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0

for i in range(n-1):
    for j in range(i + 1, n):
        # print('(', i, ',', j, ')')
        if balls[i] == balls[j]:
            continue
        else:
            cnt += 1

print(cnt)

'''
# 다른 풀이 
# 같은 수를 먼저 카운트 하고 각 경우의 수를 곱하여 계산 

# 각 무게별 공의 개수 구하기 
array = [0] * 11 # 10까지 존재한다고 문제에 명시 
for b in balls:
    array[b] += 1
    
# 경우의 수 구하기 
for b in balls:
    n -= array[b] # A가 선택할 수 있는 공의 개수를 줄여가기 
    # B가 선택할 수 있는 경우의 수와 A가 선택할 수 있는 경우의 수 더하기
    result += array[b] * n 

print(result)
'''