class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        X=[[] for i in range(n)]
        for u,v in edges:
            X[u].append(v)
            X[v].append(u)
        
        visited=[0]*n
        res=0
        for i in range(n):
            if visited[i]:
                continue
            bfs=[i]
            visited[i]=1
            for j in bfs:
                for k in X[j]:
                    if visited[k]==0:
                        bfs.append(k)
                        visited[k]=1
            if all(len(X[j])==len(bfs)-1 for j in bfs):
                res+=1
        return res

        