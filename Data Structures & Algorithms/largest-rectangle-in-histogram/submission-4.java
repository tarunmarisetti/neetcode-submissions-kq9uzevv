class Solution {
    public int largestRectangleArea(int[] heights) {
        Deque<int[]> stack=new ArrayDeque<>();
        int maxArea=0;
        int n=heights.length;
        for(int i=0; i< n; i++){
            int index=i;
            while(!stack.isEmpty() && stack.peek()[0]>heights[i]){
                int[] prevEntry=stack.pop();
                maxArea=Math.max(maxArea, prevEntry[0]*(i-prevEntry[1]));
                index=prevEntry[1];
            }
            stack.push(new int[]{heights[i],index});
        }
        
        while(!stack.isEmpty()){
            int[] entry=stack.pop();
            maxArea=Math.max(maxArea, entry[0]*(n-entry[1]));
        }
        return maxArea;
    }
}
