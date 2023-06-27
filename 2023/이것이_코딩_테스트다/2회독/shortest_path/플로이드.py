# n: 도시의 개수, m: 한 도시에서 출발하여 다른 도시에 도착하는 m 개의 버스
# (A, B)에 대해 A에서 B로 가는데 필요한 비용의 최솟값 구하기 (간선 여러개 가능)
# 플로이드 워셜 알고리즘 - 모든 지점에서 다른 모든 지점까지의 최단 경로 모두 구할 때

# 가장 짧은 간선의 정보만을 저장한 뒤 플로이드 워셜 알고리즘 수행

n = int(input())
m = int(input())

INF = int(1e9)

# graph 설정, 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 == 0
for a in range(1, n + 1):
    for b in range(1, n+ 1):
        if a == b:
            graph[a][b] = 0

# 받아온 정보로 간선 값 초기화
for _ in range(m):
    # a -> b, 비용: c
    a, b, c = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end=' ')

    print()

'''
<testCase>
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

<answer>
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
'''