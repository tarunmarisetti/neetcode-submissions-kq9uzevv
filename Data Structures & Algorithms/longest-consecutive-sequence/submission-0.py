class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len,cnt=0,0
        for num in nums:
            if num-1 not in nums:
                cnt=1
                while(num+cnt in nums):
                    cnt+=1
                max_len=max(max_len,cnt)
        return max_len
                
        