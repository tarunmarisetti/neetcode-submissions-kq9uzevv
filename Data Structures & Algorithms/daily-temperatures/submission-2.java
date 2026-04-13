class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> indxStk=new ArrayDeque<>();
        int n=temperatures.length;
        int[] res=new int[n];
        for(int i=0; i<n; i++){
            while(!indxStk.isEmpty() && temperatures[indxStk.peek()]<temperatures[i]){
                int indx=indxStk.pop();
                res[indx]=i-indx;
            }
            indxStk.push(i);
        }
        return res;
    }
}
