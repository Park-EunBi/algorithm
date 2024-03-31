def solution(participant, completion):
    hash = {}
    for p in participant:
        if p not in hash:
            hash[p] = 1
        else:
            hash[p] += 1

    for c in completion:
        hash[c] -= 1

    for h in hash:
        if hash[h]:
            return h
