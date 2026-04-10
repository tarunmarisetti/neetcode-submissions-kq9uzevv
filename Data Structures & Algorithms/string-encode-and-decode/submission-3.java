class Solution {

    public String encode(List<String> strs) {
        if(strs.isEmpty()) return "";
        StringBuilder encodedStr=new StringBuilder();
        for(String s:strs){
            encodedStr=encodedStr.append(s.length()).append('#').append(s);
        }
        return encodedStr.toString();
    }

    public List<String> decode(String str) {
        List<String> res=new ArrayList<>();
        int i=0;
        while(i<str.length()){
            int j=i;
            while(str.charAt(j)!='#'){
                j++;
            }
            int size=Integer.parseInt(str.substring(i,j));
            i=j+1;
            j=i+size;
            res.add(str.substring(i,j));
            i=j;
        }
        return res;

    }
}
