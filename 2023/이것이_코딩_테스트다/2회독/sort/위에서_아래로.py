# 수열을 내림차순으로 정렬
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

print(sorted(array, reverse= True))
