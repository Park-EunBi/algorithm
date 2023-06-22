n = int(input())

# 1번 인덱스부터 사용
# 각 인덱스에 해당하는 길이의 네트워크 선을 자르는 경우의 수를 담음
dy = [0] * (n+1)

# 직관적으로 알 수 있는 1cm, 2cm는 직접 초기화
dy[1] = 1
dy[2] = 2

# 점화식: f(n) = f(n-2) + f(n-1)
for i in range(3, n+1):
	dy[i] = dy[i-2] + dy[i-1]

print(dy[n])