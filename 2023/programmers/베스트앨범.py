def solution(genres, plays):
    # 장르별 총 재생 횟수를 해시 테이블으로
    music = {}
    recode_idx = {}
    res = []
    for idx, g in enumerate(genres):
        if g not in music:
            music[g] = plays[idx]
        else:
            music[g] += plays[idx]

        if g not in recode_idx:
            recode_idx[g] = [(idx, plays[idx])]
        else:
            recode_idx[g] += [(idx, plays[idx])]


    # 오름차순 정렬
    for (k, v) in sorted(music.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(recode_idx[k], key=lambda x:x[1], reverse=True)[:2]:
            res.append(i)

    return res

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))