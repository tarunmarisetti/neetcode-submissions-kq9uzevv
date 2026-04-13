class MyQueue {

    Deque<Integer> inStack;
    Deque<Integer> outStack;

    public MyQueue() {
        inStack=new ArrayDeque<>();
        outStack=new ArrayDeque<>();
    }
    
    public void push(int x) {
        inStack.push(x);
    }
    
    public int pop() {
        if(outStack.isEmpty()){
            populate();
        }
        return outStack.pop();
    }
    
    public int peek() {
        if(outStack.isEmpty()){
            populate();
        }
        return outStack.peek();
        
    }
    
    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }
    public void populate(){
        while(!inStack.isEmpty()){
            outStack.push(inStack.pop());
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */