# n 개의 원소로 이루어진 배열 A, B
# k 번의 바꿔치기 가능, 배열 A의 원소의 합이 최대가 되도록
# -> A의 가장 작은 원소와 B의 가장 큰 원소 교체 (a < b 일 때만)

n, k =  map(int, input().split())
a = []
b = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

'''
<testCase>
5 3
1 2 5 4 3
5 5 6 6 5

<answer>
26
'''