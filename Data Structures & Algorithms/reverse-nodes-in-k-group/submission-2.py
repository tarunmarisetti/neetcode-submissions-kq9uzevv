# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def has_k_nodes(node,k):
            while node and k>0:
                k-=1
                node=node.next
            return k==0
        
        def reverse_k_nodes(node,k):
            prev=None
            while k>0:
                nextEle=node.next
                node.next=prev
                prev=node
                node=nextEle
                k-=1
            return prev

        dummy=ListNode(0,head)
        dummyEnd=dummy
        curr=head
        while has_k_nodes(curr,k):
            start=curr
            for _ in range(k):
                curr=curr.next
            reversedList=reverse_k_nodes(start,k)
            dummyEnd.next=reversedList
            dummyEnd=start
            start.next=curr
            start=curr
        return dummy.next

        