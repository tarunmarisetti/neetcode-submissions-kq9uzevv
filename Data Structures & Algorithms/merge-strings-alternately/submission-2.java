class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder mergeStr=new StringBuilder();
        int l1=0;
        int l2=0;
        while(l1<word1.length() && l2< word2.length()){
            mergeStr.append(word1.charAt(l1)).append(word2.charAt(l2));
            l1+=1;
            l2+=1;
        }
        while(l1<word1.length()){
            mergeStr.append(word1.charAt(l1));
            l1+=1;
        }
        while(l2<word2.length()){
            mergeStr.append(word2.charAt(l2));
            l2+=1;
        }
        return mergeStr.toString();
    }
}