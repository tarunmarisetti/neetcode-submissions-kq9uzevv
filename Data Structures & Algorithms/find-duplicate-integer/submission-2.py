class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # We can use Floyd’s Cycle Detection
        # it has two phases
        # Phase:1 one is get slow and fast pointers and traverse through the list until fast and slow are equal
        slow=fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        # Phase 2 now again start from index 0 using slow2 now traverse slow1 and slow 2 
        # and the node where they intersect is the duplicated and it is forming the cycle
        slow2=0
        while True:
            slow2=nums[slow2]
            slow=nums[slow]
            if slow==slow2:
                return slow
                


        