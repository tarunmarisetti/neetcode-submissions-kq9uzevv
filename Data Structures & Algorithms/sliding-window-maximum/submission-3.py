class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        q=deque() #we store index
        left=right=0
        while right<len(nums):
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)

            if q[0]<left:
                q.popleft()
                
            if (right+1)>=k:
                res.append(nums[q[0]])
                left+=1
            right+=1
        return res
        