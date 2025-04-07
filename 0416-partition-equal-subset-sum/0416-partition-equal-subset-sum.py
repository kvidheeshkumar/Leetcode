class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        mid=total//2
        dp=[False]*(mid+1)
        dp[0]=True
        for num in nums:
            for i in range(mid,num-1,-1):
                dp[i]=dp[i] or dp[i-num]
            if dp[mid]:
                return True
        return dp[mid]

        