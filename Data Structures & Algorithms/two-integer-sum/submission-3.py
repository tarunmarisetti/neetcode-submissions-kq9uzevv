class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i,num in enumerate(nums):
            remain_value=target-num
            if remain_value in num_map:
                return [num_map[remain_value], i]
            num_map[num]=i
        return []



        