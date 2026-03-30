class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq_map=Counter(nums)
        res=[]
        for num , freq in freq_map.items():
            if freq>n//3:
                res.append(num)
        return res

        