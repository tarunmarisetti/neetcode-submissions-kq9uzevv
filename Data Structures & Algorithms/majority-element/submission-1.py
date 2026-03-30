class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_ele=None
        count=0
        for num in nums:
            if count==0:
                major_ele=num
            if num==major_ele:
                count+=1
            else:
                count-=1
        return major_ele
        