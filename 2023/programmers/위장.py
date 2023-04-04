def solution(clothes):
    # 해시 테이블 생성
    wear = {}
    for c in clothes:
        if c[1] not in wear:
            wear[c[1]] = 1
        else:
            wear[c[1]] += 1

    # 테이블의 (value + 1) 해서 다 더하고 -1
    res = 1
    for w in wear:
        res *= (wear[w] + 1)
    return res -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))