# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        min_heap=[]
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i, lst))
        
        while min_heap:
            val,index,lst=heapq.heappop(min_heap)
            curr.next=lst
            curr=curr.next
            if lst.next:
                heapq.heappush(min_heap, (lst.next.val, index, lst.next))
        return dummy.next
        