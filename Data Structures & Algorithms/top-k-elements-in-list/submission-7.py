class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        max_heap=[]
        for key, value in freq.items():
            heapq.heappush(max_heap,(value,key))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        return [key for value, key in max_heap]

        