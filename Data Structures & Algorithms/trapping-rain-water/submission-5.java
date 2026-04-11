class Solution {
    public int trap(int[] height) {
        int l=0;
        int r=height.length-1;
        int maxLeft=height[l];
        int maxRight=height[r];
        int waterTrapped=0;
        while(l<r){
            if(maxLeft<maxRight){
                l++;
                maxLeft=Math.max(maxLeft, height[l]);
                waterTrapped+=maxLeft-height[l];
            }
            else{
                r-=1;
                maxRight=Math.max(maxRight, height[r]);
                waterTrapped+=maxRight-height[r];
            }
        }
        return waterTrapped;

        
    }
}
