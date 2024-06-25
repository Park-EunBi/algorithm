def solution(babbling):
    speak = ['aya', 'ye', 'woo', 'ma']
    cnt = 0

    for ba in babbling:
        before = -1 # speak 연속 방지 idx
        now = '' # 만들어진 단어
        flag = False # 마무리 처리 (flag : True - 끝까지 발음 가능 단어로 끝남)

        for b in ba:
            if now not in speak: # speak에 속하지 않으면
                now += b # 문자 추가
                flag = False

            if now in speak: # 말 할 수 있는 단어
                if before != speak.index(now): # 연속성 체크
                    before = speak.index(now) # 인덱스 갱신
                    now = ''
                    flag = True

        if flag:
            cnt += 1

    return cnt

'''
# sol2)
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
'''