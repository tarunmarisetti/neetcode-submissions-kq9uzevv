# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        # operation for storing the pre elements before left
        left_prev=dummy
        curr=head
        for _ in range(left-1):
            left_prev=curr
            curr=curr.next
        
        # reversing the elemnets in the range(left,right)
        prev=None
        for _ in range(right-left+1):
            nextEle=curr.next
            curr.next=prev
            prev=curr
            curr=nextEle
        # Linking  the reverse sublist with the left_prev and right_next elements
        left_prev.next.next=curr
        left_prev.next=prev
        return dummy.next

        