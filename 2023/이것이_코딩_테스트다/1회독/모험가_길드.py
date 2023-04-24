n = int(input())
people = list(map(int, input().split()))

res = 0
people.sort(reverse=True)

while len(people) > 0:
    people = people[max(people):]
    res += 1
print(res)

''' 
# 다른 풀이 
people.sort()
result = 0
count = # 현재 그룹에 포함된 모험가의 수 

for i in people: 
    count += 1
    if count >= i: 
        result += 1
        count = 0
print(result)
'''