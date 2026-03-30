class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in prefix_map:
                count+=prefix_map[prefix_sum-k]
            prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
        return count

# num=2:
#     {0:1}
#     prefix_sum=2
#     count=1
#     {0:1, 2:1}
# num=-1
#     {0:1, 2:1}
#     prefix_sum=1
#     count=1
#     {0:1, 2:1, 1:1}
# num=1
#     {0:1, 2:1, 1:1}
#     prefix_sum=2
#     count=2
#     {0:1, 2:2, 1:1}

# num=2
#     {0:1, 2:2, 1:1}
#     prefix_sum=4
#     count=4
#     {0:1,2:2,1:1,4:1}



