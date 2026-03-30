class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        max_heap=[-val for val in counter.values()]
        heapq.heapify(max_heap)
        time=0
        q=deque()

        while max_heap or q:
            time+=1
            if max_heap:
                new_val=1+heapq.heappop(max_heap)
                if new_val!=0:
                    q.append((new_val,time+n))
            else:
                time=q[0][1]
            if q and q[0][1]==time:
                heapq.heappush(max_heap,q.popleft()[0])
        return time
        