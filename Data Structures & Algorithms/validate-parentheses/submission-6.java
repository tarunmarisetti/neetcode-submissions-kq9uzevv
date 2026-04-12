class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack=new ArrayDeque<>();
        Map<Character, Character> map=new HashMap<>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        for(char c: s.toCharArray()){

            if(map.containsKey(c)){
                if(stack.isEmpty() || map.get(c)!=stack.peek()){
                    return false;
                }
                stack.pop();
            }
            else stack.push(c);
        }
        return stack.isEmpty();
    }
}
