# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def has_k_nodes(curr,k):
            n=0
            while curr and n<k:
                n+=1
                curr=curr.next
            return n==k
        def reverse_K_nodes(nodes,k):
            prev=None
            while k:
                next_node=nodes.next
                nodes.next=prev
                prev=nodes
                nodes=next_node
                k-=1
            return prev


        curr=head
        dummy=ListNode(0)
        prev_end=dummy
        while has_k_nodes(curr,k):
            group_start=curr
            for _ in range(k):
                curr=curr.next
            reversed_lst=reverse_K_nodes(group_start,k)
            group_start.next=curr
            prev_end.next=reversed_lst
            prev_end=group_start
        return dummy.next

        