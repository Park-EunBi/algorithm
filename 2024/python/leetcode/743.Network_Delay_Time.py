from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 구성
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 : [(시간, 정점)]
        Q = [(0, k)]  # 초기화
        # 최단 거리 기록
        dist = defaultdict(int)

        # 다익스트라
        # 우선순위 큐 사용, 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 확인
        if len(dist) == n:
            return (max(dist.values()))
        return -1
