class Solution {
    public long putMarbles(int[] weights, int k) {
        int n=weights.length;
        long[] pairs=new long[n-1];
        for(int i=0;i<n-1;i++){
            pairs[i]=(long)weights[i]+weights[i+1];
        }
        Arrays.sort(pairs,0,n-1);
        long res=0l;
        for(int i=0;i<k-1;i++){
            res+=pairs[n-2-i]-pairs[i];
        }
        return res;
    }
}