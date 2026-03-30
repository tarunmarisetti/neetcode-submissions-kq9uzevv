class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums)
        res=[]
        for num,freq in freq_map.items():
            heapq.heappush(res,(freq,num))
            if len(res)>k:
                heapq.heappop(res)
        return [num for freq, num in res]

        