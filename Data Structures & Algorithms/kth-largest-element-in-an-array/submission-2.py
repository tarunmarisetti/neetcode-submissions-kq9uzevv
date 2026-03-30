class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLargest=[]
        for num in nums:
            if len(kLargest)==k:
                heapq.heappushpop(kLargest, num)
            else:
                heapq.heappush(kLargest, num)
        return kLargest[0]
                