class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy / BFS-style solution:
        # Each jump represents a "level".
        # [l, r] is the range of indices reachable with current jumps.
        # For all indices in this range, compute the farthest index reachable
        # with one more jump.
        # Move to the next range and increment jump count.

        l=r=0
        farthest=0
        res=0
        while r<len(nums)-1:
            for i in range(l, r+1):
                farthest=max(farthest, i+nums[i])
            l=r+1
            r=farthest
            res+=1
        return res
        