def solution(number, limit, power):
    score = [1 for _ in range(number + 1)]

    # 에라토스테네스의 체를 응용 해 봄
    # 자신의 배수인 수는 해당 수의 값의 += 1
    for i in range(1, number + 1):
        for j in range(i * 2, number + 1, i):
            score[j] += 1

    return sum([
        power
        if score[i] > limit # 제한보다 크면 power 더하기
        else score[i] # 아니면 score[i] 더하기
        for i in range(1, number + 1)
    ])

'''
# sol2)
def solution(number, limit, power):
    divisor_num = []
    for j in range(1, number+1):
        cnt = 0
        for i in range(1, int(j**0.5) +1 ): # 약수는 짝이 있음을 이용 
            if (j == i**2):
                cnt +=1
            elif (j%i == 0):
                cnt +=2
        divisor_num.append(cnt)
    res = [i if i <= limit else power for i in divisor_num ]
    return sum(res)
'''