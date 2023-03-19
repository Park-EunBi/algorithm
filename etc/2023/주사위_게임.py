import sys
sys.stdin = open("input.txt", "rt")

# 3개의 주사위
# 같은 눈 3개 -> 10,000 + (같은 눈) * 1,000원
# 같은 눈 2개 -> 1,000 + (같은 눈) * 100원
# 모두 다른 눈 -> (가장 큰 눈) * 100원
# n명이 주사위 게임에 참여했을 때 가장 많은 상금을 받는 사람

n = int(input()) # 참여자 수
games = []
for _ in range(n):
    games.append(list(map(int, input().split())))

res = []

for dice in games:
    # 같은 수가 몇 개인지 세는 게 중요
    # -> set 사용
    same_num = len(set(dice))
    if same_num == 1:
        res.append(10000 + (dice[0]) * 1000)
    elif same_num == 2:
        # 같은 눈이 뭔지 찾기
        find_num = [0] * 7
        for i in dice:
            find_num[i] += 1
        res.append(1000 + (find_num.index(2)) * 100)
    else:
        res.append(max(dice) * 100)
print(max(res))

'''
# 다른 풀이 

max=0
res=0
n=int(input())
for i in range(n):
    tmp=input().split() 
    tmp.sort() 
    a, b, c=map(int, tmp)
    if a==b and b==c: # 3개의 수가 같은지 확인 
        money=10000+(a*1000);
    elif a==b or a==c: # 2개의 수가 같은지 확인 
        money=1000+(a*100)
    elif b==c: # 2개의 수가 같은지 확인 
        money=1000+(b*100)
    else: # 모든 수가 다름 
        money=c*100
    if money > res:
        res=money

print(res)
'''