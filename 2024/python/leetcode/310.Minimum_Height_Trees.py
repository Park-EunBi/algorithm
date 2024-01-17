class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = [
            []
            for _ in range(n + 1)
        ]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        # 첫 번째 리프노드 추기
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트노드만 남을 때 까지 반복
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves