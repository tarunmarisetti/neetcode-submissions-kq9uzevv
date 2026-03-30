class MedianFinder:

    def __init__(self):
        self.small_heap=[]
        self.large_heap=[]


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap,-num)
        heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        if len(self.small_heap)<len(self.large_heap):
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))
        

    def findMedian(self) -> float:
        if len(self.small_heap)>len(self.large_heap):
            return -self.small_heap[0]
        else:
            return (-self.small_heap[0]+self.large_heap[0])/2
        
        