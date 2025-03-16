from bisect import bisect_left
from typing import List
from math import sqrt
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_time_sufficient(t:int)->bool:
            return sum(int(sqrt(t//rank)) for rank in ranks)>=cars
        max_time=ranks[0]*cars*cars
        min_time_required=bisect_left(range(max_time),True,key=is_time_sufficient)
        return min_time_required
        