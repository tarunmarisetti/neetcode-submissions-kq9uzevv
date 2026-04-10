class Solution {
    private static class Entry{
        int key;
        int val;
        
        Entry(int key, int val){
            this.key=key;
            this.val=val;
        }
    }
    
    public int[] topKFrequent(int[] nums, int k) {
        PriorityQueue<Entry> queue=new PriorityQueue<>((a,b)-> a.val - b.val);
        HashMap<Integer, Integer> map=new HashMap<>();
        for(int num:nums){
            map.put(num, map.getOrDefault(num,0)+1);
        }
        for(Map.Entry<Integer,Integer> entry: map.entrySet()){
            Entry entryObj=new Entry(entry.getKey(),entry.getValue());
            queue.offer(entryObj);
            if(queue.size()>k){
                queue.poll();
            }
        }
        int[] res=new int[k];
        int indx=0;
        while(!queue.isEmpty()){
            Entry entry=queue.poll();
            res[indx++]=entry.key;

        }
        return res;
    }
   
}
