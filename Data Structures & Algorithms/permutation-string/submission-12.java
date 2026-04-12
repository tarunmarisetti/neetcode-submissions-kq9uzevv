class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s2.length()<s1.length()){
            return false;
        }
        Map<Character, Integer> s1FreqMap=new HashMap<>();
        for(char c:s1.toCharArray()){
            s1FreqMap.put(c, s1FreqMap.getOrDefault(c,0)+1);
        }
        Map<Character, Integer> windowFreq=new HashMap<>();
        int left=0;
        for(int right=0; right<s2.length();right++){
            char currChar=s2.charAt(right);
            windowFreq.put(currChar, windowFreq.getOrDefault(currChar,0)+1);
            if(right-left+1>s1.length()){
                char leftChar=s2.charAt(left);
                windowFreq.put(leftChar, windowFreq.getOrDefault(leftChar,0)-1);
                if(windowFreq.get(leftChar)==0){
                    windowFreq.remove(leftChar);
                }
                left+=1;
            }
            if(windowFreq.equals(s1FreqMap)){
                return true;
            }
        }
        return false;
    }
}
