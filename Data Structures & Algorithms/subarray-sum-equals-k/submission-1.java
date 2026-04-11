class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixCountMap=new HashMap<>();
        prefixCountMap.put(0,1);
        int prefix=0;
        int subArrayCount=0;
        for(int i=0;i<nums.length;i++){
            prefix+=nums[i];
            if(prefixCountMap.containsKey(prefix-k)){
                subArrayCount+=prefixCountMap.get(prefix-k);
            }
            prefixCountMap.put(prefix,prefixCountMap.getOrDefault(prefix,0)+1);
        }

        return subArrayCount;
        
    }
}