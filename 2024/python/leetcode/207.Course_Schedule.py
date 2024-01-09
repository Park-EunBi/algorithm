from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        # 순환구조 판단
        traced = set()
        visited = set()

        def dfs(node):
            # 이미 traced에 존재하면 재방문 했다는 뜻 -> 순환 구조
            if node in traced:
                return False

            # 방문했다면 다시 확인할 필요 없음 -> 가지치기
            if node in visited:
                return True

            # traced에 존재하지 않으면 add
            traced.add(node)
            for g in graph[node]:
                if not dfs(g):
                    return False

            # 방문후 반드시 노드 제거 (형제노드간 관련성 생성됨)
            traced.remove(node)
            # 방문처리
            visited.add(node)

            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True