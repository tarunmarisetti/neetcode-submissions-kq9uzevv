class FreqStack {
    Map<Integer, Integer> freqMap;
    Map<Integer, Deque<Integer>> groupMap;
    int maxFreq;

    public FreqStack() {
        freqMap=new HashMap<>();
        groupMap=new HashMap<>();
        maxFreq=0;
    }
    
    public void push(int val) {
        int freq=freqMap.getOrDefault(val,0)+1;
        freqMap.put(val,freq);
        groupMap.putIfAbsent(freq, new ArrayDeque<>());
        groupMap.get(freq).push(val);
        maxFreq=Math.max(maxFreq, freq);
    }
    
    public int pop() {
        int res=groupMap.get(maxFreq).pop();
        freqMap.put(res, freqMap.get(res)-1);
        if(groupMap.get(maxFreq).isEmpty()){
            maxFreq-=1;
        }
        return res;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */