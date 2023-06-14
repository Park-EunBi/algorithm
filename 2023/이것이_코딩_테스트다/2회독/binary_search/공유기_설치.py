# p.369, baekjoon 2110
# 한 집에는 공유기 하나만, 가장 인접한 공유기 사이의 거리를 가능한 크게
# n: 집의 개수, c: 공유기 개수
# 파라메트릭 서치

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()

start = 1 # 설치 가능한 최소 거리
end = houses[-1] - houses[0] # 설치 가능한 최대 거리
result = 0

while start <= end:
    # 가장 인접한 두 공유기 사이 거리
    mid = (start + end) // 2
    value = houses[0]
    # 설치한 공유기의 개수 세기
    count = 1

    # 공유기 설치
    for i in range(1, n): # n: 집의 개수
        # 집이 이전 집 + mid (떨어진 값) 보다 멀리 있다면
        if houses[i] >= value + mid:
            value = houses[i] # 다음 집 좌표 넣기
            count += 1
    # 지정된 공유기 개수 보다 더 많이 설치 가능하다면
    if count >= c:
        start = mid + 1 # 거리 증가
        result = mid # 거리 저장
    # 지정된 공유기 개수 보다 더 적게 설치 가능하다면
    else:
        end = mid -1 # 거리 줄이기
print(result)


'''
<testCase>
5 3
1
2
8
4
9

<answer>
3
'''
