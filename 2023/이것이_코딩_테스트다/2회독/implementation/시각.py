# n이 입력되면 n시 59분 59까지 모든 시각 중
# 3이 하나라도 포함되는 모든 경우의 수 구하기

n = int(input())
# n = 5

# 직접 세기
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # if str(s) in '3': 으로 작성하지 않도록 주의!
            if '3' in str(h) + str(m) + str(s):
                    count += 1
print(count)


