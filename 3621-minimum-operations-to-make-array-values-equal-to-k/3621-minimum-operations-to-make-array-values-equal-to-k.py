class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hashmap=defaultdict(int)
        for i in nums:
            if i<k:
                return -1
            elif i>k:
                hashmap[i]+=1
        return len(hashmap)
        