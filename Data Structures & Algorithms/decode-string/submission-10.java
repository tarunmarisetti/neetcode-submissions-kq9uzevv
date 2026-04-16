class Solution {
    public String decodeString(String s) {
        Deque<String> stack=new ArrayDeque<>();
        for(char c: s.toCharArray()){
            StringBuilder encodedStr=new StringBuilder();
            StringBuilder multiplier=new StringBuilder();
            if(c==']'){
                while(!stack.isEmpty() && !stack.peek().equals("[")){
                    encodedStr.insert(0,stack.pop());
                }
                stack.pop();
                while(!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))){
                    multiplier.insert(0,stack.pop());
                }
                
               
                int num=Integer.parseInt(multiplier.toString());
                
                String newStr=encodedStr.toString().repeat(num);

                stack.push(newStr);
            }
            else{
                stack.push(String.valueOf(c));
            }
        }
        StringBuilder res=new StringBuilder();
        while(!stack.isEmpty()){
            res.insert(0,stack.pop());
        }
        
        return res.toString();
    }
}