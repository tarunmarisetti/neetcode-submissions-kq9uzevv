class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen=new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int remainSum=target-nums[i];
            if(seen.containsKey(remainSum)){
                return new int[]{seen.get(remainSum),i};
            }
            seen.put(nums[i],i);
        }
        return new int[0];
    }
    
}
