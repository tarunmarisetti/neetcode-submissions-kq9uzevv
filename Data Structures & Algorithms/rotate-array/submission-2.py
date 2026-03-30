class Solution:
    def helper(self,nums,l,r):
        while l<r:
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        self.helper(nums,0,n-1)
        self.helper(nums,0,k-1)
        self.helper(nums,k,n-1)

        