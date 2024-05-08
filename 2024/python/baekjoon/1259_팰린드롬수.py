while 1:
    s = input()
    if s == '0':
        break

    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            print('no')
            break
    else:
        print('yes')