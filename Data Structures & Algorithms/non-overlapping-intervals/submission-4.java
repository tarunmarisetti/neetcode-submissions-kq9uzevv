class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a,b)->Integer.compare(a[0],b[0]));
        int minRemovals=0;
        int[] prevInterval=intervals[0];
        for(int i=1; i<intervals.length; i++){
            int start=intervals[i][0];
            int end=intervals[i][1];
            if(start<prevInterval[1]){
                minRemovals+=1;
                prevInterval[1]=Math.min(prevInterval[1], end);
            }
            else{
                prevInterval=intervals[i];
            }
        }
        return minRemovals;
    }
}
