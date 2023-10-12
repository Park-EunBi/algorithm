s = input()
n = len(s)
# 펠린드롬 검사
def pel(s):
    return s == s[::-1]


idx = 0 # insert 값 포인터
while 1:
    # 펠린드롬이면 break
    if pel(s):
        print(len(s))
        break
    else:
        # insert 해서 팰린드롬 만들기
        # 1. list 로 변경
        s = list(s)
        # 2. 원래 문자가 끝나는 부분에 거꾸로 문자 삽입
        s.insert(n, s[idx])
        # 3. 문자열로 변경
        s = ''.join(s)
        # 4. 삽입할 문자 변경
        idx += 1


