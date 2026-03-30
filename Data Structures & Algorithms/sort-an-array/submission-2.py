class Solution:
    def mergeSort(self,nums,left,right):
        if left>=right:
            return
        mid=(left+right)//2
        self.mergeSort(nums,left,mid)
        self.mergeSort(nums,mid+1,right)
        self.merge(nums,left,mid,right)

    def merge(self,nums,left,mid,right):
        L=nums[left:mid+1]
        R=nums[mid+1:right+1]
        i,j=0,0
        k=left
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                nums[k]=L[i]
                i+=1
            else:
                nums[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            nums[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            nums[k]=R[j]
            j+=1
            k+=1

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums
        