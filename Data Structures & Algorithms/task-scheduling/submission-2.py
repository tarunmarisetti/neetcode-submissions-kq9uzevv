class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq=defaultdict(int)
        for task in tasks:
            taskFreq[task]+=1
        maxHeap=[-val for val in taskFreq.values()]
        heapq.heapify(maxHeap)
        time=0
        q=deque()

        while maxHeap or q:
            time+=1
            if maxHeap:
                newCount=1+heapq.heappop(maxHeap)
                if newCount<0:
                    q.append((time+n, newCount))
            while q and q[0][0]<=time:
                heapq.heappush(maxHeap,q.pop()[1])
        return time
        