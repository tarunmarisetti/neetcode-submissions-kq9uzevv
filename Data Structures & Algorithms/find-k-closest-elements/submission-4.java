class Solution {
    private static class Entry{
        int dist;
        int val;

        Entry(int dist, int val){
            this.dist=dist;
            this.val=val;
        }
    }
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        PriorityQueue<Entry> queue=new PriorityQueue<>(
            (a,b)->{
                if(a.dist==b.dist){
                    return b.val-a.val;
                }
                return b.dist-a.dist;
                });

        for(int num : arr){
            int dist=Math.abs(num-x);
            queue.offer(new Entry(dist,num));
            if(queue.size()>k){
                queue.poll();
            }
        }
        List<Integer> res=new ArrayList<>();
        while(!queue.isEmpty()){
            res.add(queue.poll().val);
        }
        Collections.sort(res);
        return res;
    }
}