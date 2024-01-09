from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        # 풀이 1 - 재귀
        ret = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop(0))
            ret.append(node)

        '''    
        # 풀이 2 - 반복문
        ret, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            ret.append(stack.pop())
        '''

        dfs('JFK')
        return ret[::-1]