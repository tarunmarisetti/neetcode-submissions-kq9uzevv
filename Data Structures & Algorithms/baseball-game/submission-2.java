class Solution {
    public int calPoints(String[] operations) {
        Deque<Integer> stack=new ArrayDeque<>();
        for(String s: operations){
            if(s.equals("+")){
                int last=stack.pop();
                int secondLast=stack.peek();
                stack.push(last);
                stack.push(last+secondLast);
            }
            else if(s.equals("D")){
                stack.push(stack.peek()*2);
            }
            else if(s.equals("C")){
                stack.pop();
            }
            else{
                stack.push(Integer.parseInt(s));
            }
        }
        int res=0;
        while(!stack.isEmpty()){
            res+=stack.pop();
        }
        return res;
    }
}