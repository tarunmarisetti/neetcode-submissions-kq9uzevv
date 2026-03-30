class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd=1
        rightProd=1
        left_sum=[1]*len(nums)
        ans=[1]*len(nums)
        for i in range(len(nums)):
            left_sum[i]=leftProd
            leftProd*=nums[i]
        print(left_sum)
        for i in range(len(nums)-1, -1, -1):
            ans[i]=left_sum[i]*rightProd
            rightProd*=nums[i]
        return ans


        