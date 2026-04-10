class Solution {
    public void sortColors(int[] nums) {
        int red=0;
        int white=0;
        int blue=0;
        for(int num: nums){
            if(num==0){
                red+=1;
            }
            else if(num==1){
                white+=1;
            }
            else{
                blue+=1;
            }
        }
        int index=0;
        for(int i=0;i<red;i++){
            nums[index++]=0;
        }
        for(int i=0;i<white;i++){
            nums[index++]=1;
        }
        for(int i=0;i<blue;i++){
            nums[index++]=2;
        }
    }
}