class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        main_p=m+n-1
        nums1_p,nums2_p=m-1,n-1
        while nums2_p>=0 and nums1_p>=0:
            if nums1[nums1_p]>nums2[nums2_p]:
                nums1[main_p]=nums1[nums1_p]
                nums1_p-=1
            else:
                nums1[main_p]=nums2[nums2_p]
                nums2_p-=1
            main_p-=1
        while nums2_p>=0:
            nums1[main_p]=nums2[nums2_p]
            nums2_p-=1
            main_p-=1
        
        