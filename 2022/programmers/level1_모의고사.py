def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if (answers[i] == one[i%len(one)]):
            score[0] += 1
        if (answers[i] == two[i % len(two)]):
            score[1] += 1
        if (answers[i] == three[i % len(three)]):
            score[2] += 1
    m = max(score)
    answer = [i + 1 for i, v in enumerate(score) if v == m]

    return answer

'''
[런타임 에러]
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt = []
    answer = []
    for i in range(len(answers)):
        if answers[i] == one[len(one) % (i + 1)]:
            cnt1 += 1
        if answers[i] == two[len(two) % (i + 1)]:
            cnt2 += 1
        if answers[i] == three[len(three) % (i + 1)]:
            cnt3 += 1
    cnt.append(cnt1)
    cnt.append(cnt2)
    cnt.append(cnt3)

    m = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == m:
            answer.append(i+1)

    return answer
'''

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))