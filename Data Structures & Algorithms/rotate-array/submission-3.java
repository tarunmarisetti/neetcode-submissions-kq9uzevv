class Solution {
    public void rotateHelper(int l, int r, int[] nums){
        while(l<r){
            int temp=nums[l];
            nums[l]=nums[r];
            nums[r]=temp;
            l+=1;
            r-=1;
        }
    }
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        rotateHelper(0, n-1, nums);
        rotateHelper(0, k-1, nums);
        rotateHelper(k,n-1, nums);
    }
}