class Solution {
    public List<Integer> partitionLabels(String s) {
        int n=s.length();
        int[] alphabet=new int[26];
        for(int i=0;i<n;i++){
            alphabet[s.charAt(i)-'a']=i;
        }
        List<Integer> res=new ArrayList<>();
        int start=0,end=-1;
        for(int i=0;i<n;i++){
            end=Math.max(end,alphabet[s.charAt(i)-'a']);
            if(i==end){
                res.add(end-start+1);
                start=i+1;
            }
        }
        return res;
    }
}