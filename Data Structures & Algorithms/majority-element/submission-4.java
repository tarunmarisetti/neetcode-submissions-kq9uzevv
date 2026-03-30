class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map=new HashMap<>();
        for(int num : nums){
            map.putIfAbsent(num,0);
            map.put(num,map.get(num)+1);
        }
        int n=nums.length;
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int key=entry.getKey();
            int value=entry.getValue();
            if (value>n/2){
                return key;
            }
        }
        return -1;
    }
}