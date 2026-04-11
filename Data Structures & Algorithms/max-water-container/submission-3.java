class Solution {
    public int maxArea(int[] heights) {
        int l=0;
        int r=heights.length-1;
        int maxArea=0;
        while(l<r){
            int currArea=Math.min(heights[l],heights[r])*(r-l);
            maxArea=Math.max(currArea, maxArea);
            if(heights[l]<heights[r]){
                l+=1;
            }
            else{
                r-=1;
            }
        }
        return maxArea;
    }
}
