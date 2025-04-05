class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res|=i
        return res*(1<<(len(nums)-1))
        