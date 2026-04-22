/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


class Solution {
    private static class Entry{
        int val;
        int index;
        ListNode node;

        Entry(int val, int index, ListNode node){
            this.val=val;
            this.index=index;
            this.node=node;
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Entry> minHeap=new PriorityQueue<>((a,b)->{
            if(a.val==b.val){
                return Integer.compare(a.index, b.index);
            }
            return Integer.compare(a.val, b.val);
        });
        ListNode dummy=new ListNode();
        ListNode curr=dummy;
        int i=0;
        for(ListNode list: lists){
            if (list!=null){
                minHeap.offer(new Entry(list.val,i,list));
            }
           i++;
        }
        while(!minHeap.isEmpty()){
            Entry currEntry=minHeap.poll();
            int val=currEntry.val;
            int index=currEntry.index;
            ListNode node=currEntry.node;
            curr.next=node;
            curr=curr.next;
            if(node.next!=null){
                minHeap.offer(new Entry(node.next.val, index, node.next));
            }
        }
        return dummy.next;
    }
}
