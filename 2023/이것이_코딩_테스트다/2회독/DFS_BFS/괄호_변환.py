# https://school.programmers.co.kr/learn/courses/30/lessons/60058
# '(', ')'의 개수가 같다면 "균형잡힌 괄호 문자열"
# 짝까지 맞을 경우 "올바른 괄호 문자열"
# "균형잡힌 괄호 문자열"이 주어질 때, "올바른 괄호 문자열"로 변환한 결과 반환

# "균형잡힌 괄호 문자열"의 index 반환
def balanced_index(p):
    count = 0  # 왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:  # ')' 인 경우
            count -= 1
        if count == 0:
            return i


# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            # '(' 으로 시작되지 않는 경우
            if count == 0:
                return False  # 쌍이 맞지 않는 경우
            count -= 1
        return True  # 쌍이 맞는 경우


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    # "올바른 괄호 문자열" 인 경우
    if check_proper(u):
        answer = u + solution(v)

    # 아니라면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer