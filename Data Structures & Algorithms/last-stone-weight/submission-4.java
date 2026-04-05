class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap=new PriorityQueue<>((a,b)-> b-a);
        for(int stone: stones){
            maxHeap.offer(stone);
        }
        while(maxHeap.size()>1){
            int stone1=maxHeap.poll();
            int stone2=maxHeap.poll();
            if(stone1!=stone2){
                maxHeap.offer(Math.abs(stone1-stone2));
            }
        }
        return maxHeap.size()==1 ? maxHeap.peek(): 0;
    }
}
