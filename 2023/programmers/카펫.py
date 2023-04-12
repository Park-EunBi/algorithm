def solution(brown, yellow):
    # ((brown -4)/2 -y) y = yellow
    # x = yellow / y
    # return x + 2, y + 2

    for i in range(brown):
        if ((brown - 4) / 2 - i) * i == yellow:
            y = i
            x = yellow / y
            return [x + 2, y + 2]

# print(solution(10, 2))
# print(solution(8, 1))
# print(solution(24, 24))