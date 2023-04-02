def solution(participant, completion):
    # 완주하지 못한 선수의 이름을 리턴
    # participant를 해시로 만든다
    par = {}
    for p in participant:
        if p not in par:
            par[p] = 1
        else:
            par[p] +=1

    # completion이 존재하면 -= 1
    for c in completion:
        par[c] -= 1

    for d in par:
        if par[d] == 1:
            return d

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))