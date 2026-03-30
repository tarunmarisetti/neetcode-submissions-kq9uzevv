class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod=[0]*len(nums)
        lprod=1
        for i in range(len(nums)):
            left_prod[i]=lprod
            lprod*=nums[i]

        rprod=1
        for i in range(len(nums)-1, -1, -1):
            left_prod[i]*=rprod
            rprod*=nums[i]
        return left_prod

        