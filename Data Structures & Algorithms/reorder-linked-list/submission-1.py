# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        # reverse the second half
        prev=None
        while curr:
            next_ele=curr.next
            curr.next=prev
            prev=curr
            curr=next_ele
        
        #iterate the two lists
        first,second=head,prev
        while second:
            temp1,temp2=first.next, second.next
            first.next=second
            second.next=temp1
            first,second=temp1,temp2

        