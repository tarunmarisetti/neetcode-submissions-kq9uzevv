class Solution:
    def rotate_helper(self,nums,l,r):
        while l<r:
            nums[l], nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        return nums
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        self.rotate_helper(nums,0,n-1)
        self.rotate_helper(nums,0, k-1)
        self.rotate_helper(nums, k, n-1)

        
        

        