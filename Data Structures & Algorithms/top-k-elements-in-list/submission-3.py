class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums)
        res=[]
        seen=set()
        heapq.heapify(res)
        for num in nums:
            if num not in seen:
                heapq.heappush(res,(freq_map[num],num))
                seen.add(num)
            if len(res)>k:
                heapq.heappop(res)
        return [num for freq, num in res]

        