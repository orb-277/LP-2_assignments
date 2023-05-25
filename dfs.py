from collections import deque

class Graph:
    def __init__(self,n:int) -> None:
        self.n = n
        self.adjlist = [[] for i in range(n)]
    def addedge(self,src:int,dest:int):
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)

    def rec_dfs(self,vertex,visited):
        if vertex not in visited:
            visited.append(vertex)
            print(vertex,end=" ")
            for u in self.adjlist[vertex]:
                self.rec_dfs(u,visited)
    def dfs(self,vertex):
        visited = []
        self.rec_dfs(vertex,visited)
    def bfs(self,vertex):
        q = deque()
        visited = []
        q.append(vertex)
        visited.append(vertex)
        while(q):
            v = q.popleft()
            print(v,end=" ")
            for i in self.adjlist[v]:
                if i not in visited:
                    visited.append(i)
                    q.append(i)





            






g = Graph(5)
g.addedge(0,1)
g.addedge(1,3)
g.addedge(2,4)
g.addedge(3,4)
#g.dfs(0)
g.bfs(0)

                







