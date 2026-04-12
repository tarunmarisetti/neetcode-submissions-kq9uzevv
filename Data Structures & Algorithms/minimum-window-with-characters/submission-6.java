class Solution {
    private static class Res{
        int len;
        int[] range;

        Res(int len, int l, int r){
            this.len=len;
            this.range=new int[]{l,r};
        }
    }

    public String minWindow(String s, String t) {
        Map<Character, Integer> tCounter=new HashMap<>();
        Map<Character, Integer> windowCounter=new HashMap<>();
        for(char c: t.toCharArray()){
            tCounter.put(c, tCounter.getOrDefault(c,0)+1);
        }
        int left=0;
        int have=0;
        Res res=new Res(Integer.MAX_VALUE,0,0);
        int need=tCounter.size();
        for(int right=0; right<s.length(); right++){
            char currChar=s.charAt(right);
            windowCounter.put(currChar, windowCounter.getOrDefault(currChar,0)+1);
            if(tCounter.containsKey(currChar) && tCounter.get(currChar)==windowCounter.get(currChar)){
                have++;
            }
            while(have==need){
                if(res.len>(right-left+1)){
                    res.len=(right-left+1);
                    res.range=new int[]{left,right};
                }
                char leftChar=s.charAt(left);
                windowCounter.put(leftChar, windowCounter.getOrDefault(leftChar,0)-1);
                if(tCounter.containsKey(leftChar) && windowCounter.get(leftChar)<tCounter.get(leftChar)){
                    have--;
                }
                left++;

            }
        }
        return res.len!=Integer.MAX_VALUE ? s.substring(res.range[0], res.range[1]+1) : "";
   }
}
