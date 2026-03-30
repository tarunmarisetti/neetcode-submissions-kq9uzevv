class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs==null || strs.length==0) return "";
        String lcp=strs[0];
        for(int i=1; i<strs.length; i++){
            while(!strs[i].startsWith(lcp)){
                lcp=lcp.substring(0, lcp.length()-1);
                if (lcp.isEmpty()) return "";
            }
        }
        return lcp;
    }
}