# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        secondList=slow.next
        slow.next=None

        # reverese the second list
        prev=None
        while secondList:
            nextEle=secondList.next
            secondList.next=prev
            prev=secondList
            secondList=nextEle
        
        # merging two lists
        start=head
        while start and prev:
            temp1,temp2=start.next,prev.next
            start.next=prev
            prev.next=temp1
            start,prev=temp1,temp2


        