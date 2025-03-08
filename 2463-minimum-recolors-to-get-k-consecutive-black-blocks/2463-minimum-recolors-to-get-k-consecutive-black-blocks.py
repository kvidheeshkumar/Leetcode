class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        start=0
        end=n
        min_count=0
        count=0
        for i in range(start,k):
            if blocks[i]=='W':
                count+=1
        min_count=count
        start=k
        while start<end:
            if blocks[start]=='W':
                count=count+1
            if blocks[start-k]=='W':
                count=count-1
            min_count=min(count,min_count)
            start+=1
        return min_count
            


        