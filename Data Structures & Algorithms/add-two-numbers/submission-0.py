# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem=0
        dummy=ListNode(0)
        curr=dummy
        while l1 or l2 or rem:
            l1_val=l1.val if l1 else 0
            l2_val=l2.val if l2 else 0
            rem,currSum=divmod(l1_val+l2_val+rem,10)
            node=ListNode(currSum)
            curr.next=node
            curr=curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next


        