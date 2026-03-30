class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_counter=defaultdict(int)
        res=[]
        for i in range(len(nums)+1-k):
            window=nums[i:i+k]
            max_num=max(window)
            res.append(max_num)
        return res
        