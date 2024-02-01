class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))

        ret = []
        while heap:
            person = heapq.heappop(heap)
            ret.insert(person[1], (-person[0], person[1]))
        return ret