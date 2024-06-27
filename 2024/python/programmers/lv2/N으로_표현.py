def solution(N, number):
    # (n을 k번 사용해 만들 수 있는 수) (연산자 4가지) (n을 n-k번 사용해 만들 수 있는 수)
    dp = [set([int(str(N) * i)]) for i in range(1, 9)]  # idx: n 사용 횟수
    # [{5}, {0, 1, 10, 55, 25}, {0, 2, 4, 5, 6, 555, -20, -4, -50, 15, 11, 50, 275, 20, -5, 60, 125, 30}...

    print(dp)
    # n 사용 횟수
    for i in range(8):  # 최대 활용 횟수
        for j in range(i):  # 좌측
            # j 개
            for num1 in dp[j]:
                # i-j 개
                for num2 in dp[i - j - 1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        if number in dp[i]:
            return i + 1

    return -1