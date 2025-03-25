class Solution {
    public boolean check(List<Pair<Integer, Integer>> a, int n) {
        List<Pair<Integer, Integer>> temp=new ArrayList<>();
        temp.add(a.get(0));
        for(int i=1;i<n;i++){
            if(a.get(i).getKey()>=temp.get(temp.size()-1).getValue())
              temp.add(a.get(i));
            else
              temp.set(temp.size()-1, new Pair<>(temp.get(temp.size()-1).getKey(),Math.max(temp.get(temp.size()-1).getValue(),a.get(i).getValue())));
        }
        return temp.size()>=3;
    }
    public boolean checkValidCuts(int n, int[][] rectangles){
        int m=rectangles.length;
        List<Pair<Integer, Integer>> x=new ArrayList<>();
        List<Pair<Integer, Integer>> y=new ArrayList<>();
        for(int[] r:rectangles){
            x.add(new Pair<>(r[0],r[2]));
            y.add(new Pair<>(r[1],r[3]));
        }
        Collections.sort(x, Comparator.comparing(Pair::getKey));
        Collections.sort(y, Comparator.comparing(Pair::getKey));
        return check(x,m)||check(y,m);
    }
}