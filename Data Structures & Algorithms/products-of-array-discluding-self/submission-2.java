class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int[] res= new int[n];
        for(int i=0;i<n;i++){
            res[i]=1;
        }
        int leftProd=1;
        for(int i=1;i<n;i++){
            leftProd*=nums[i-1];
            res[i]=leftProd;
        }
        int rightProd=1;
        for(int i=n-2; i>=0; i--){
            rightProd*=nums[i+1];
            res[i]*=rightProd;
        }
        return res;
        
    }
}  
