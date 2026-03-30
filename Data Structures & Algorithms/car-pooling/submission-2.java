class Solution {
    public boolean carPooling(int[][] trips, int capacity) {

        Arrays.sort(trips, Comparator.comparingInt(a->a[1]));
        // min heap
        PriorityQueue<int[]> minHeap= new PriorityQueue<>
        (Comparator.comparingInt(a->a[0]));

        int currCapacity=0;
        for(int[] trip:trips){
            int passengers=trip[0];
            int start=trip[1];
            int end=trip[2];
            while(!minHeap.isEmpty() && minHeap.peek()[0]<=start){
                currCapacity-=minHeap.poll()[1];
            }
            currCapacity+=passengers;
            if(currCapacity>capacity){
                return false;
            }
            minHeap.offer(new int[]{end, passengers});
        }
        return true;
        
    }
}