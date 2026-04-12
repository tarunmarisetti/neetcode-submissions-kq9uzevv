class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> seen=new HashSet<>();
        int left=0;
        int longestSubStringLen=0;
        for(int right=0; right<s.length(); right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left+=1;
            }
            seen.add(s.charAt(right));
            longestSubStringLen=Math.max(longestSubStringLen, (right-left+1));
        }
        return longestSubStringLen;
    }
}
