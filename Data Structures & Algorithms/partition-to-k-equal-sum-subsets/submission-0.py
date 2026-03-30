class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        isUsed=[False]*n
        totalSum=sum(nums)
        if totalSum%k!=0:
            return False
        target=totalSum//k
        def dfs(i,subSetSum,k):
            if k==0:
                return True
            if subSetSum==target:
                return dfs(0,0, k-1)
            
            for j in range(i,n):
                if isUsed[j] or subSetSum+nums[j]>target:
                    continue
                isUsed[j]=True
                if dfs(j+1,subSetSum+nums[j],k):
                    return True
                isUsed[j]=False
            return False
        return dfs(0,0,k)

