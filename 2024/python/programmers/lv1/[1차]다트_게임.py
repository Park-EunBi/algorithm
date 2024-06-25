def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    score = [0, 0, 0]
    num = ''
    idx = 0

    for dart in dartResult:

        # 숫자면 문자열로 더하기 (10 있어서)
        if dart.isdigit():
            num += dart

        # 알파벳이면 점수 계산
        elif dart.isalpha():
            score[idx] = int(num) ** bonus[dart]
            num = '' # 문자열 num 초기화
            idx += 1 # 다음 점수판

        else: # 옵션이면
            if dart == '*':
                if idx - 2 >= 0: # 알파벳에서 idx += 해줘서 -2
                    score[idx - 2] *= 2
                score[idx - 1] *= 2

            elif dart == '#':
                score[idx - 1] = -score[idx - 1]

    return sum(score)