class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        res=0
        end=0
        for start, finish in meetings:
            if start>end:
                res+=start-end-1
            end=max(end,finish)
        if days>end:
            res+=days-end
        return res
        