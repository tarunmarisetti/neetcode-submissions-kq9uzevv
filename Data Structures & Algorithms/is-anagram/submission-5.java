class Solution {
    
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap<Character,Integer> sHash=new HashMap<>();
        HashMap<Character,Integer> tHash=new HashMap<>();

        for(int i=0; i<s.length(); i++){
            char ch=s.charAt(i);
            sHash.put(ch, sHash.getOrDefault(ch,0)+1);
        }
        for(int i=0; i<t.length(); i++){
            char ch=t.charAt(i);
            tHash.put(ch, tHash.getOrDefault(ch,0)+1);
        }
       
        for(Map.Entry<Character, Integer> entry: sHash.entrySet()){
            char key=entry.getKey();
            if(!entry.getValue().equals(tHash.get(key))){
                return false;
            }
        }
        return true;
    }
}

