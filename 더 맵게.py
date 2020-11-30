#level2_Heap

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for element in scoville:
        heapq.heappush(heap, element)
        
    while heap[0] < K:
        try:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            heapq.heappush(heap,  first + (second*2))
            
        except IndexError:
            return -1
        answer += 1
        
    return answer
