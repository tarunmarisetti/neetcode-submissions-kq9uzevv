class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> freqMap=new HashMap<>();
        int left=0;
        int maxFreq=0;
        int longestSubStringLen=0;
        for(int right=0; right<s.length();right++){
            char currChar=s.charAt(right);
            freqMap.put(currChar, freqMap.getOrDefault(currChar,0)+1);
            maxFreq=Math.max(maxFreq, freqMap.get(currChar));
            while(((right-left+1)-maxFreq)>k){
                freqMap.put(s.charAt(left), freqMap.getOrDefault(s.charAt(left),0)-1);
                left+=1;
            }
            longestSubStringLen=Math.max(longestSubStringLen, (right-left+1));
        }
        return longestSubStringLen;

    }
}
