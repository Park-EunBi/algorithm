def solution(answers):
    # 찍는 방식 저장
    one = (1, 2, 3, 4, 5)
    two = (2, 1, 2, 3, 2, 4, 2, 5)
    three = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)

    numbers = [one, two, three]

    # 점수 계산
    answer = []
    for n in numbers:
        score = 0
        for i, a in enumerate(answers):
            length = len(n)
            if a == n[i % length]:
                score += 1
        answer.append(score)

    # max 값 출력하기
    maximum = max(answer)
    # print(maximum)
    result = []
    for i, a in enumerate(answer):
        if a == maximum:
            result.append(i + 1)

    return result