class Solution {
    public int longestConsecutive(int[] nums) {
        int maxSeq=0;
        Set<Integer> numsSet=new HashSet<>();
        for(int num: nums){
            numsSet.add(num);
        }

        for(int num: numsSet){
            int count=1;
            if(!numsSet.contains(num-1)){
                while(numsSet.contains(num+count)){
                    count+=1;
                }
            }
            maxSeq=Math.max(maxSeq, count);
        }
        return maxSeq;
    }
}
