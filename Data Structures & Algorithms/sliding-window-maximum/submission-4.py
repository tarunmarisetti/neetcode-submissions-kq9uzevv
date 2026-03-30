class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        l,r=0,0
        res=[] # store index

        while r<len(nums):
            # before appending the index we should remove all the index which has value less than curr index
            # in this way the max ele in the curr window will always be at first pos of q
            while q and nums[q[-1]] <nums[r]:
                q.pop()
            # now append the curr_index
            q.append(r)

            if q[0]<l:
                q.popleft()
            if(r+1)>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res


        