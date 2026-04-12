class MyStack {

    Deque<Integer> queue1;
    Deque<Integer> queue2;

    public MyStack() {
        queue1=new ArrayDeque<>();
        queue2=new ArrayDeque<>();
    }
    
    public void push(int x) {
        queue2.offer(x);
        while(!queue1.isEmpty()){
            queue2.offer(queue1.poll());
        }
        Deque<Integer> temp=queue1;
        queue1=queue2;
        queue2=temp;


    }
    
    public int pop() {
       return  queue1.poll();
    }
    
    public int top() {
       return queue1.peek();
        
    }
    
    public boolean empty() {
        return queue1.isEmpty();
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */