class TimeMap {
    private static class Entry{
        int timeStamp;
        String val;

        Entry(int timeStamp, String val){
            this.timeStamp=timeStamp;
            this.val=val;
        }
    }

    Map<String, List<Entry>> store;

    public TimeMap() {
        store=new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        store.putIfAbsent(key, new ArrayList<>());
        store.get(key).add(new Entry(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        if(!store.containsKey(key)){
            return "";
        }
        List<Entry> currEntryList=store.get(key);
        String res=binarySearch(currEntryList, timestamp);
        return res;
    }
    public String binarySearch(List<Entry> entryList, int timestamp){
        int left=0;
        int right=entryList.size()-1;
        String res="";
        while(left<=right){
            int mid=(left+right)/2;
            Entry currEntry=entryList.get(mid);
            if(currEntry.timeStamp<timestamp){
                res=currEntry.val;
                left=mid+1;
            }
            else if(currEntry.timeStamp>timestamp){
                right=mid-1;
            }
            else{
                return currEntry.val;
            }
        }
        return res;
    }
}
