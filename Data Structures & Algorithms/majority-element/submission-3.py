class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_ele=None
        count=0
        for num in nums:
            if count==0:
                majority_ele=num
            if num==majority_ele:
                count+=1
            else:
                count-=1
        return majority_ele
        