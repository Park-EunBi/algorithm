def solution(d, budget):
    d.sort()

    for idx, money in enumerate(d):
        budget -= money

        if budget < 0:
            return idx

    return len(d) # 예산이 남을 경우
