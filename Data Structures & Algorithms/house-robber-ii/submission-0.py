class Solution:
    def rob(self, nums: List[int]) -> int:
        # this probelm issimilar to house rob we need to use the robber 1 logic as a function here 
        # as we need to pass two subarrays one is nums[1:] excluding 1 st house or nums[:-1] excluding last house 
        # cause we cant rob the side by side houses (here the houses are circular)
        def robhelper(nums):
            rob1=rob2=0
            for house in nums:
                temp=max(rob1+house, rob2)
                rob1=rob2
                rob2=temp
            return rob2
        return max(robhelper(nums[1:]), robhelper(nums[:-1]),nums[0])
        # here in the final return we are using nums[0] cause this is an edge case what if the input is only one house 