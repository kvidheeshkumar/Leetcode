class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        count=Counter(n for arr in grid for n in arr)

        for i in count:
            if(grid[0][0]-i)%x:
                return -1
        arr, prev, curr, minC, maxC=[],0,0,min(count),max(count)

        for n in range(minC, maxC+1,x):
            arr.append(prev+curr)
            prev,curr=arr[-1],curr+count[n]

        res,curr,nxt=inf,0,0

        for n in range(maxC, minC-1, -x):
            res=min(res,arr.pop()+curr+nxt)
            curr,nxt=curr+count[n],curr+nxt
        return res
        