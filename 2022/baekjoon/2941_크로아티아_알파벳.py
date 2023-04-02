cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
alpha = input()

for i in cro:
    if i in alpha:
        '''
        alpha = alpha.replace(i, '') 
        res += 1
        발견한 크로아티아 문자를 없애면
        중복된 크로아티아 문자를 셀 수 없다. 
        '''
        alpha = alpha.replace(i, "*") 
        # 두 글자 이상의 크로아티아 문자를 한번에 *로 변경하여 글자 수를 셀 수 있다.

print(len(alpha))

'''
runtime error (index error)

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
start = ["c", "d", "l", "n", "s", "z"]

alpha = input()
jump = 0
res = 0
for i in range(len(alpha)):
    if jump >= 1:
        jump -= 1
        continue

    else:
        if i < len(alpha):
            if alpha[i] in start:
                if(alpha[i+1] == "z"):
                    if(alpha[i+2] == "="):
                        res += 1
                        jump = 2

                elif alpha[i]+alpha[i+1] in cro:
                    res += 1
                    jump = 1
                else:
                    res += 1
            else:
                res += 1

print(res)
'''