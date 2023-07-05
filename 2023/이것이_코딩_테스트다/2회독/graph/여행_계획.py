# n 개의 여행지 (1 부터 시작)
# 도로로 연결되어 있다면 양방향 이동 가능 의미
# 여행 계획이 가능한지 여부 판단

# 서로소 집합 알고리즘 사용
# 여행 계획에 해당하는 모든 노드가 같은 집합에 속하면 가능한 여행 경로
# 노드 사이에 도로가 존재하는 경우 합집합 (union) 연산 사용하여 연결된 노드를 같은 집합에 속하도록
# 여행 계획에 속하는 모든 노드가 같은 집합인지 확인하면 된다

def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
n, m = map(int, input().split())
parent = [0] * (n + 1)

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# union 연산 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결 된 경우 union 연산
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력
plan = list(map(int, input().split()))

result = True

# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m -1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

# 여행 계획 속 모든 노드가 연결되어 있는지 확인 (루트 동일 확인)
if result:
    print('YES')
else:
    print('NO')