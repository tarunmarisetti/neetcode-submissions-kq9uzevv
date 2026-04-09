class Solution {
    public String longestCommonPrefix(String[] strs) {
        String longestPrefix=strs[0];
        for(int i=1; i<strs.length; i++){
            String currString=strs[i];
            int minLen=Math.min(longestPrefix.length(), currString.length());
            int indx=0;
            while(indx<minLen && longestPrefix.charAt(indx)==currString.charAt(indx)){
                indx+=1;
            }
            longestPrefix=longestPrefix.substring(0, indx);
            if(longestPrefix.isEmpty()) return "";
        }
        return longestPrefix;
    }
}