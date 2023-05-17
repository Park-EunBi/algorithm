# 2명이 게임 수행, 1번부터 시작
# 타워 높이 % 제거 높이 == 0 혹은 제거한 높이가 1이 되도록 제거 가능
# 모든 타워의 높이가 1이면 패배

def towerBreakers(n, m):
    return 2 if n % 2 == 0 or m == 1 else 1