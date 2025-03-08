class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        seen=[]
        repeat=0
        missing=0
        for i in range(n):
            temp=grid[i]
            for j in temp:
                if j not in seen:
                    seen.append(j)
                else:
                    repeat=j
        s=n*n
        s=(s*(s+1))//2
        missing=s-sum(seen)
                
        return [repeat, missing]
        

