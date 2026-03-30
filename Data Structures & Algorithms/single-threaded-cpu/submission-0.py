from collections import deque
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q=deque()
        min_heap=[]
        for i,task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda x:(x[0],x[1]))

        for startTime, processingTime, indx in tasks:
            q.append((processingTime, indx, startTime))
        
        res=[]
        time=q[0][2]
        while min_heap or q:
            while q and q[0][2]<=time:
                heapq.heappush(min_heap, q.popleft())
            
            if min_heap:
                processingTime, indx, startTime=heapq.heappop(min_heap)
                res.append(indx)
                time=time+processingTime
            else:
                time=q[0][2]
        return res