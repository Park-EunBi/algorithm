def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''

    for char in s:
        # 공백 처리
        if char == ' ':
            ans += ' '
            continue

        upper = False
        if char.isupper():
            upper = True
            char = char.lower()

        idx = (alpha.index(char) + n) % len(alpha)

        char = alpha[idx]

        if upper:
            char = char.upper()

        ans += char

    return ans

'''
# sol2)
def caesar(s, n):
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
            
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
'''