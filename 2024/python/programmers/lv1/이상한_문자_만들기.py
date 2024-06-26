def solution(s):
    ans = ''
    idx = 0
    s = s.lower() # 숨겨진 조건 찾아내기

    for char in s:
        if char == ' ':
            idx = 0
            ans += char
            continue

        if not idx % 2:
            ans += (char.upper())
        else:
            ans += char
        idx += 1

    return ans

'''
# sol2)
def toWeirdCase(s):
    res = []
    for x in s.split(' '): # 공백을 기준으로 문자를 나누어 이중 for 문 
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)
'''