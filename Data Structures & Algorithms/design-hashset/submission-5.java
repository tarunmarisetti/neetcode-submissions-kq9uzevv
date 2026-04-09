class MyHashSet {
    private static class ListNode{
        int key;
        ListNode next;

        ListNode(int key){
            this.key=key;
        }
    }
    private final ListNode[] memory;

    public MyHashSet() {
        memory=new ListNode[10000];
        
    }

    public void add(int key) {
        int hash=key % memory.length;
        ListNode curr=memory[hash];
        if(curr==null){
            memory[hash]=new ListNode(key);
            return;
        }
        while(curr!=null){
            if(curr.key==key) return;
            if(curr.next==null){
                curr.next=new ListNode(key);
                return;
            }
            curr=curr.next;
        }        
    }
    
    public void remove(int key) {
        int hash=key % memory.length;
        ListNode curr=memory[hash];
        if(curr==null) return;
        ListNode prev=null;
        while(curr!=null){
            if(curr.key==key){
                if(prev!=null){
                    prev.next=curr.next;
                }
                else{
                    memory[hash]=curr.next;
                }
                return;
            }
            prev=curr;
            curr=curr.next;
        }

    }
    
    public boolean contains(int key) {
        ListNode curr=memory[key % memory.length];
        if(curr==null) return false;
        while(curr!=null){
            if(curr.key==key){
                return true;
            }
            curr=curr.next;
        }
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */