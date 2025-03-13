class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        m=len(queries)
        prefix=[0]*(n+1)
        current=0
        idx=0
        for i,num in enumerate(nums):
            current+=prefix[i]
            while idx<m and current<num:
                left,right,val=queries[idx]
                idx+=1
                if i<left:
                    prefix[left]+=val
                elif i<=right:
                    current+=val
                prefix[right+1]-=val
            if current<num:
                return -1
        return idx