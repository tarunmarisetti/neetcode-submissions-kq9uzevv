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
                else if(top==Math.abs(asteroid)){
                    stack.pop();
                    isAlive=false;
                    break;
                }
            }
            if(isAlive){
                stack.push(asteroid);
            }
        }
        int[] res=new int[stack.size()];
        int index=0;
        while(!stack.isEmpty()){
            res[index++]=stack.pop();
        }

        int l=0;
        int r=res.length-1;
        while(l<r){
            int temp=res[l];
            res[l]=res[r];
            res[r]=temp;
            l++;
            r--;
        }
        return res;
    }
}