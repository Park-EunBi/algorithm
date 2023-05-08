# 공포도가 x 인 모험가는 반드시 x명 이상으로 구성된 그룹에 참여
# 최대 몇 개의 그룹을 만들 수 있는지

n = int(input())
scary = list(map(int, input().split()))

scary.sort(reverse=True)

# 가장 겁이 많은 사람부터 인덱싱해서 뽑아냄
result = 0
while len(scary) >= 1:
    scary = scary[scary[0]:]
    result += 1
print(result)

'''
<다른 풀이 - 교재> 
result = 0
# 그룹 안에 포함된 사람의 수 
count = 0

# 공포도가 낮은 것 부터 
for i in scary:
    # 그룹에 포함시키기 
    count += 1
    # 그룹에 들어간 사람의 수 보가 공포도 보다 크다면 
    # (== 사람을 더 넣지 않아도 된다)
    if count >= i:
        # 그룹 개수 증가 
        result += 1
        # 그룹 안에 들어간 사람 수 리셋 
        count = 0
'''


'''
<testCase>
5
2 3 1 2 2
<answer>
2
'''