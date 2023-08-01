# n 명의 모험가
# 공포도가 x 인 모험가는 반드시 x 명 이상으로 구성한 모험가 그룹에 참여해야 한다
# 그룹 수의 최댓값을 구하는 프로그램 작성

n = int(input())
people = list(map(int, input().split()))

people.sort(reverse=True)

cnt = 0

while len(people) > 1:
    people = people[people[0]:]
    cnt += 1

print(cnt)