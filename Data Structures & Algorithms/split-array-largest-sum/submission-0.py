class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(total):
            subarray=1
            currSum=0
            for num in nums:
                currSum+=num
                if currSum >total:
                    '''here if the curr ele is not fitting in the subarray 
                    then we are creating another subarray and starting the currsum with that ele
                    eg:[1,2,3,4,10], total=10
                    so we can have [1,2,3,4] caue the sum is 10 <=10
                    but if we try to add next ele 10 the subarraysum is exceeding the total
                    so we create new subarray and start the currsum from that ele which is 10'''
                    subarray+=1
                    currSum=num
            return subarray<=k

        # this proble is similar to ship container problem

        '''here the lower bound is we can split just by taking on ele in subarray
        and the subarray which has max sum is--> max(nums)
        for,upper bound here we split th array such that we got all the ele in a subarray
        so the sum is all elements-->sum(nums)'''
        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            mid=(l+r)//2
            if canSplit(mid):
                res=mid
                r=mid-1  #we need to minimise the sum so we should move toward left
            else:
                l=mid+1
        return res
        