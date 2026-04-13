class MinStack {

    private static class Entry{
        int num;
        int minVal;

        Entry(int num, int minVal){
            this.num=num;
            this.minVal=minVal;
        }
    }

    Deque<Entry> minStack;
  

    public MinStack() {
        minStack=new ArrayDeque<>();
    }
    
    public void push(int val) {
        int min=minStack.isEmpty() ? val : Math.min(val, minStack.peek().minVal);
        minStack.push(new Entry(val, min));
    }
    
    public void pop() {
        minStack.pop();
    }
    
    public int top() {
        return minStack.peek().num;
    }
    
    public int getMin() {
        return minStack.peek().minVal;
    }
}
