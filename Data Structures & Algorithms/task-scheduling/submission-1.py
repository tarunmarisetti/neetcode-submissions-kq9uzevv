class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap=[]
        totalTime=0
        counter={}
        for task in tasks:
            if task not in counter:
                counter[task]=0
            counter[task]+=1

        for val in counter.values():
            heapq.heappush(maxHeap, -val)

        q=deque()
        while maxHeap or q:
            totalTime+=1
            if maxHeap:
                newValue=1+heapq.heappop(maxHeap)
                if newValue<0:
                    q.append((totalTime+n, newValue))
            else:
                totalTime=q[0][0]
            while q and q[0][0]<=totalTime:
                heapq.heappush(maxHeap, q.popleft()[1])
        return totalTime
            
