class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indexMap=new HashMap<>();
        for(int i=0; i<nums.length;i++){
            int remainSum=target-nums[i];
            if(indexMap.containsKey(remainSum)){
                return new int[]{indexMap.get(remainSum),i};
            }
            indexMap.put(nums[i], i);
        }
        return new int[]{-1,-1};
    }
}
