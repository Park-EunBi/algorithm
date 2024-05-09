while 1:
    string = list(input())
    if len(string) == 1:
        break

    flag = 'yes'
    q = []
    for s in string:
        if s == '(' or s == '[':
            q.append(s)
        elif s == ')':
            if len(q):
                if q[-1] == '(':
                    q.pop()
                else:
                    flag = 'no'
                    break
            else: # 놓치지 않도록 주의하기
                flag = 'no'
                break

        elif s == ']':
            if len(q):
                if q[-1] == '[':
                    q.pop()
                else:
                    flag = 'no'
                    break
            else:
                flag = 'no'
                break

    if len(q):
        flag = 'no'

    print(flag)