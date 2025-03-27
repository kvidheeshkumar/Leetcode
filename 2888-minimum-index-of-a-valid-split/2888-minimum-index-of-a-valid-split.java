class Solution {
    public int minimumIndex(List<Integer> nums) {
        int n=nums.size();
        int count=0;
        int idx=-1;
        for(int i:nums){
            if(count==0){
                idx=i;
            }
            count+=(i==idx)?1:-1;
        }
        Map<Integer, Integer> freq=new HashMap<>();
        for(int i:nums){
            freq.put(i,freq.getOrDefault(i,0)+1);
        }
        int countFreq=0;
        for(int i=0;i<n;i++){
            countFreq+=(nums.get(i)==idx)?1:0;
            if(countFreq*2>(i+1) && (freq.get(idx)-countFreq)*2>(n-i-1)){
                return i;
            }
        }
        return -1;
    }

}