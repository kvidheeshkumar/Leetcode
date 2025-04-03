from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet_value=0
        max_number=0
        max_diff=0
        for number in nums:
            max_triplet_value=max(max_triplet_value,max_diff*number)
            max_number=max(max_number,number)
            max_diff=max(max_diff,max_number-number)
        return max_triplet_value
        