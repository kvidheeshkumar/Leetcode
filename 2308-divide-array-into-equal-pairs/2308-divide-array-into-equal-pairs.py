class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a=0
        nums.sort()
        n=len(nums)
        i=0
        while i<n-1:
            if nums[i]==nums[i+1]:
                a+=1
                i+=2
            else:
                i+=1
        if a==n//2:
            return True
        else:
            return False
        
        