class Solution {
    public long mostPoints(int[][] questions) {
        int n=questions.length;
        long[] total=new long[n];
        long prev=questions[n-1][0];

        for(int i=n-1;i>=0;i--){
            total[i]=prev;
            long point=questions[i][0];
            int skip=questions[i][1];
            int j=i+skip+1;
            if(j<n){
                point+=total[j];
            }
            if(point>prev){
                total[i]=point;
            }
            prev=total[i];
        }
        return total[0];
    }
}