# 지정 길이보다 길면 -> 지정 길이
# 지정 길이보다 짧으면 -> 원래 길이
# 손님은 짤린 길이를 가져감
# m : 요청한 길이, n : 떡의 개수
# 적어도 m 만큼 가져가기 위해서 설정할 수 있는 높이의 최댓값

n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)

# binary_search
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in rice_cake:
        if x > mid:
            # 잘리고 남은 부분 추가
            total += x - mid
    # 아직 요청 길이에 도달하지 못했다면 다시 칼의 길이 설정
    if total < m:
        end = mid -1
    # 요청 길이에 도달시
    else:
        # 결과 저장
        result = mid
        # 다시 탐색
        start = mid + 1
print(result)

'''
<testCase>
4 6
19 15 10 17

<answer>
15
'''