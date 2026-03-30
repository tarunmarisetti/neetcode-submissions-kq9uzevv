class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right=0,len(nums)-1
        while (left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            # the sol is samae as the search in rotated sorted array but here tehre are duplicate elemenst 
            # so we need to add this check eg:[1,0,1,1,1] what if all the l,r, mid are equal so we need to shift l, r by 1
            elif nums[left]==nums[right]==nums[mid]:
                left+=1
                right-=1

            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False
        