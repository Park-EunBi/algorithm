# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트가 아니면 루트 찾을 때 까지 재귀
    if parent[x] != x: # idx와 값이 같으면 root
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # 각 원소의 root를 찾음
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 작은 값으로 연결
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
# input
v, e = map(int, input().split()) # 노드 개수, 간선
parent = [0] * (v + 1)

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')

'''
6 4
1 4
2 3
2 4
5 6

각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 11115 5
'''