class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0
        if n==3:
            product=(nums[0]-nums[1])*nums[2]
            if product>0:
                return product
            else:
                return 0
        if n>3:
            product=0
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        if (nums[i]-nums[j])*nums[k]>product:
                            product=(nums[i]-nums[j])*nums[k]
            return product
        