def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            # return 2개 사용
            return participant[i]
    return participant[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

'''
[typeerror: Object of type set is not JSON serializable]

participant, completion = set(participant), set(completion)
return list(participant - completion)
 
-> answer = list(participant - completion)
   return answer[0] 
   typeerror는 해결했으나 동명이인이 있을 때의 상황을 해결하지 않음 (문제를 끝까지 잘 읽기)
'''

'''
[효율성 검사: 시간 초과]

def solution(participant, completion):
    for c in completion:
        if c in participant:
            participant.remove(c)
    return participant[0]
'''

'''
[다른 풀이_1]
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''

'''
[다른 풀이_2]
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
'''