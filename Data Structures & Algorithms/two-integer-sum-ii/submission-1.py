class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen_map={}
        for i,num in enumerate(numbers, start=1):
            rem=target-num
            if rem in seen_map:
                return [seen_map[rem],i]
            seen_map[num]=i
        # print(seen_map)
        return [-1,-1]
        