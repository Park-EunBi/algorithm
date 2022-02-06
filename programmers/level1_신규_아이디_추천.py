import re
def solution(new_id):
    # 소문자 변환
    # A-Za-z0-9\-\_\. 에 포함되지 않는 문자 제거
    answer = re.sub("[^A-Za-z0-9\-\_\.]", "", new_id.lower())
    # 2개 이상 . 등장시 제거
    answer = re.sub("\.{2,1000}", ".", answer)
    # 양 끝단 문자열 삭제
    answer = answer.strip(".")
    # 빈문자열이면 a 대입
    if(len(answer) < 1):
        answer = "a"
    # 길이가 16 이상이면 첫 15개 제외 모두 제거
    elif (len(answer) >= 16):
        answer = answer[:15]
        answer = answer.strip(".")
    # 글자수가 2 이하일 때 마지막 문자 추가
    if (len(answer) <= 2):
        while(len(answer) < 3):
            answer = answer + answer[-1:]

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))