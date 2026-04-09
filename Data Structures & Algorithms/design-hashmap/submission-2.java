class MyHashMap {
    private static class ListNode{
        int key;
        int value;
        ListNode next;
        ListNode(int key, int value){
            this.key=key;
            this.value=value;
        }
    }
    private final ListNode[] memory;
    private int size;

    public MyHashMap() {
        size=10000;
        memory=new ListNode[size];
        
    }
    
    public void put(int key, int value) {
        int hash=key % size;
        ListNode curr= memory[hash];
        if (curr==null){
            memory[hash]=new ListNode(key, value);
            return;
        }
        while(curr!=null){
            if(curr.key==key){
                curr.value=value;
                return;
            }
            if(curr.next==null){
                curr.next=new ListNode(key, value);
                return;
            }
            curr=curr.next;
        }

    }
    
    public int get(int key) {
        int hash=key % size;
        ListNode curr= memory[hash];
        if (curr==null) return -1;
        while(curr!=null){
            if(curr.key==key){
                return curr.value;
            }
            curr=curr.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        int hash=key % size;
        ListNode curr= memory[hash];
        if (curr==null) return;
        ListNode prev=null;
        while(curr!=null){
            if(curr.key==key){
                if(prev!=null){
                    prev.next=curr.next;
                    return;
                }
                memory[hash]=curr.next;
            }
            prev=curr;
            curr=curr.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */