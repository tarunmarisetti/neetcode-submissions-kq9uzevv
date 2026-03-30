# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_k_nodes(curr,k):
            prev=None
            while curr and k>0:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
                k-=1
            return prev,curr

        def has_k_nodes(curr,k):
            while curr and k>0:
                k-=1
                curr=curr.next
            return k==0


        dummy=ListNode(0,head)
        prev_end=dummy
        curr=head
        while has_k_nodes(curr,k):
            start=curr
            
            reversed_pair_head, next_segment=reverse_k_nodes(start,k)
            prev_end.next=reversed_pair_head
            start.next=next_segment
            prev_end=start
            curr=next_segment
        return dummy.next
            


        