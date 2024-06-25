import heapq
def solution(k, score):
    heap = []
    answer = []

    # for i in range(k): # k > len(score) 일 때 오류
    for i in range(min(k, len(score))):
        heapq.heappush(heap, score[i])
        answer.append(min(heap))

    for i in range(k, len(score)):
        if min(heap) < score[i]:
            heapq.heappop(heap)
            heapq.heappush(heap, score[i])
        answer.append(min(heap))

    return answer

'''
# sol2)
def solution(k, scores):
    from heapq import heappushpop, heappush

    answer = []
    hq = []
    for idx, score in enumerate(scores):
        if idx >= k:
            heappushpop(hq, score)
        else:
            heappush(hq, score)

        answer.append(hq[0])
    return answer
    
# sol3)
def solution(k, score):
    q = []
    answer = []
    
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer
'''