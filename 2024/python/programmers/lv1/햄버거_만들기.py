def solution(ingredient):
    answer = 0
    s = []

    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                s.pop()

    return answer
'''
# 프로그래머스에서 안돌아감
def solution(ingredient):
    answer = 0

    tmp = ingredient
    end = False

    while not end:
        for p in range(len(tmp) - 3):
            print(p)
            # 슬라이싱: O(n)
            if tmp[p] == 1 and tmp[p + 1] == 2 and tmp[p + 2] == 3 and tmp[p + 3] == 1:
                tmp.pop(p)
                tmp.pop(p)
                tmp.pop(p) # pop 3개부터 안돌아감...
                tmp.pop(p)

                answer += 1
                print(p, tmp)
                break

            if p == len(tmp) - 4:
                end = True
                break

    return answer

s = solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
print(s)
'''