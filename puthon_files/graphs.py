## Adjacency List:
from collections import defaultdict
def makeGraph(connections):
            graph = defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph


			
t=[[0,1],[0,2],[0,3],[2,4],[3,5]]

t=makeGraph(t)
# print(t)
print(dfs_iterative(0,t))
print(dfs_recursive(0,t,set(),0))


