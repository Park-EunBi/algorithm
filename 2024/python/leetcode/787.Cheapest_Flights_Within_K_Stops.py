import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [
            []
            for _ in range(n + 1)
        ]

        for a, b, w in flights:
            graph[a].append((b, w))

        q = [(0, src, k)]

        while q:
            time, node, k = heapq.heappop(q)
            if node == dst:
                return time
            if k >= 0:
                for v, w in graph[node]:
                    cost = time + w
                    heapq.heappush(q, (cost, v, k - 1))

        return -1