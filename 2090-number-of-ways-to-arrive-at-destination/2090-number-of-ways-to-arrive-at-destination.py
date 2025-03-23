class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v,time in roads:
            graph[u].append((v,time))
            graph[v].append((u,time))
        
        MOD=10**9+7
        distance=[float('inf')]*n

        count=[0]*n
        distance[0]=0
        count[0]=1

        priorityQueue=[(0,0)]

        while priorityQueue:
            curr, u=heapq.heappop(priorityQueue)
            if curr>distance[u]:
                continue
            for v, time in graph[u]:
                new_path=curr+time
                if new_path<distance[v]:
                    distance[v]=new_path
                    count[v]=count[u]
                    heapq.heappush(priorityQueue,(new_path,v))
                elif new_path==distance[v]:
                    count[v]+=count[u]
                    count[v]%=MOD
        return count[n-1]
        