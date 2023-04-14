# 두 팀의 능력치 차이를 최소로 하기
from itertools import combinations
n = int(input())
team= [] # 각 능력치
for i in range(n):
    team.append(list(map(int, input().split())))


# n/2의 수로 팀을 만들고
# 각 팀에 속하는 사람들의 능력치의 합을 구하고 능력치의 최소 값을 반환

# 사람 번호
# 팀을 나눠서 뽑힌 사람과 그렇지 않은 사람으로 나눌 것
people = [i for i in range(n)]

# 스타트 팀과 링크 팀 나누기
start_team = []
start_team.extend(combinations(people, n//2))
# start 팀에 속하지 않은 사람이 링크 팀

# start 팀에 속한 사람과 link 팀에 속한 사람의 경험치의 합을 구하면 된다
# start 팀에 속한 사람들의 경험치의 합
# 여기서 또 2개 씩 모아서 합을 구해야 한다

start_point = 0
link_point = 0
start = [] # 합을 구하기 위해 start 사람 2명씩 짝 지은 것
link = [] # 합을 구하기 위해 link 사람 2명씩 짝 지은 것
small = 99999999
for s in start_team:
    start = []
    link = []
    start.extend(list(combinations(s, 2)))

    # 링크 팀의 조합
    l = tuple(set(people) - set(s))
    # 링크 팀의 합의 조합을 구하기
    link.extend(list(combinations(l, 2)))

    start_point = 0
    link_point = 0

    # 각 팀의 경험치의 합을 구하면 된다
    for i, j in start:
        start_point += team[i][j] # start 팀 조합 1의 경험치 합
        start_point += team[j][i] # start 팀 조합 2의 경험치 합

    for i, j in link:
        link_point += team[i][j] # link 팀 조합 1의 경험치 합
        link_point += team[j][i] # link 팀 조합 2의 경험치 합

    # 두 경험치의 차가 가장 작은 거 반환
    small = min(small, abs(start_point - link_point))

print(small)



