class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack=new ArrayDeque<>();
        for(int asteroid: asteroids){
            boolean isAlive=true;
            while(!stack.isEmpty() && stack.peek()>0 && asteroid<0){
                int top=stack.peek();
                if(top<Math.abs(asteroid)){
                    stack.pop();
                }
                else if(top>Math.abs(asteroid)){
                    isAlive=false;
                    break;
                }
                else{
                    stack.pop();
                    isAlive=false;
                    break;
                }
            }
            if(isAlive){
                stack.push(asteroid);
            }
        }
        int n=stack.size();
        int[] res=new int[n];
        int index=n-1;
        while(!stack.isEmpty()){
            res[index--]=stack.pop();
        }
        return res;
    }
}