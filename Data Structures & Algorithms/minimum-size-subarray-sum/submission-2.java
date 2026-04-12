class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int prefix=0;
        int left=0;
        int minSize=Integer.MAX_VALUE;
        for(int right=0; right<nums.length; right++){
            prefix+=nums[right];
            while(prefix>=target){
                minSize=Math.min(minSize, (right-left+1));
                prefix-=nums[left];
                left+=1;
            }
        }
        return minSize!=Integer.MAX_VALUE ? minSize :0;
        
    }
}