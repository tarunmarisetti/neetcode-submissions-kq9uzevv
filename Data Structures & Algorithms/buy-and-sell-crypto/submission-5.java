class Solution {
    public int maxProfit(int[] prices) {
        int buy=prices[0];
        int sell=0;
        for(int i=1; i<prices.length;i++){
            if(prices[i]<buy){
                buy=prices[i];
            }
            else{
                sell=Math.max(sell, prices[i]-buy);
            }
        }
        return sell;
    }
}
