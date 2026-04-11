class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int currIndex=m+n-1;
        int n1=m-1;
        int n2=n-1;
        while(n1>=0 && n2>=0){
            if(nums1[n1]>nums2[n2]){
                nums1[currIndex]=nums1[n1];
                n1-=1;
            }
            else{
             nums1[currIndex]=nums2[n2];
             n2-=1;
            }
            currIndex-=1;
        }
        while(n1>=0){
            nums1[currIndex]=nums1[n1];
            n1-=1;
            currIndex-=1;
        }
        while(n2>=0){
            nums1[currIndex]=nums2[n2];
            n2-=1;
            currIndex-=1;

        }
    }
}