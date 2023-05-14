# 일정 단위로 잘라 단어 압축하기
# 가장 짧은 문자의 길이 리턴
# 가장 앞부터 정해진 길이만큼 리턴
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    # 압축하는 길이를 증가시켜가며 최소 값을 찾으면 된다
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        # 압축할 문자열
        prev = s[:step]
        count = 1

        # step 만큼 증가시키면서 문자열 비교
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            # 압축이 끝나면
            else:
                compressed += str(count) + prev if count >= 2 else prev
                # prev if count >= 2 else prev
                # count >= 2 가 참이면 compressed += str(count) + prev, 아니면 prev
                # 초기화
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        # 문자열이 가장 짧은 것
        answer = min(answer, len(compressed))

    return answer
