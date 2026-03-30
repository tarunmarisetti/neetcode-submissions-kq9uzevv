class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            # case 1: mid is target
            if nums[mid]==target:
                return mid

            #case2: usually for the rotated sorted array one side must be in sorting order 
            # here we are checking that
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            # case 3: the ele is in the right part the array
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
            
        