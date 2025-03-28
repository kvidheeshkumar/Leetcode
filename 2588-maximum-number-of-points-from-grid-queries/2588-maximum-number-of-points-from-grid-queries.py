from heapq import heappop, heappush
from itertools import pairwise

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols=len(grid), len(grid[0])
        sorted_queries=sorted((value,index) for index, value in enumerate(queries))
        results=[0]*len(sorted_queries)
        priority_queue=[(grid[0][0],0,0)]
        points_count=0
        visited=[[False]*cols for _ in range(rows)]
        visited[0][0]=True

        for value, index in sorted_queries:
            while priority_queue and priority_queue[0][0]<value:
                _, current_row, current_col=heappop(priority_queue)
                points_count+=1
                for delta_row, delta_col in pairwise((-1,0,1,0,-1)):
                    adjacent_row, adjacent_col=current_row+delta_row, current_col+delta_col
                    if 0<=adjacent_row<rows and 0<=adjacent_col<cols and not visited[adjacent_row][adjacent_col]:
                        heappush(priority_queue, (grid[adjacent_row][adjacent_col],adjacent_row,adjacent_col))
                        visited[adjacent_row][adjacent_col]=True
            results[index]=points_count
        return results