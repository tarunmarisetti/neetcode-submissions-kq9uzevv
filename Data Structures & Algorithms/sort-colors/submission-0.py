class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color1_count=color2_count=color3_count=0
        for num in nums:
            if num==0:
                color1_count+=1
            elif num==1:
                color2_count+=1
            else:
                color3_count+=1
        nums[:color1_count]=[0]*color1_count
        nums[color1_count:color1_count+color2_count]=[1]*color2_count
        nums[color1_count+color2_count:]=[2]*color3_count


        