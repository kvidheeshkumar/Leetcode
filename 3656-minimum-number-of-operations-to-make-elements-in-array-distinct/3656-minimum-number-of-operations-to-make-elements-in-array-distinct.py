class Solution:
    def check(self,d):
        for i in d:
            if d[i]>1:
                return False
        return True
    def minimumOperations(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        while self.check(d)==False and len(nums)>0:
            if len(nums)<=3:
                return count+1
            if len(nums)>3:
                count+=1
                d[nums[0]]-=1
                nums.pop(0)
                d[nums[0]]-=1
                nums.pop(0)
                d[nums[0]]-=1
                nums.pop(0)
        return count
        


        