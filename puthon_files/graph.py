
from collections import defaultdict
def makeGraph(connections):
            graph = defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph
t=[[1,3],[2,3],[3,1]]

graph=makeGraph(t)


N=5
plantdict = {i: 0 for i in range(1, N + 1)}
print(plantdict)

pick = set(range(1,5))
print(pick.pop())




#find the element with N-1 incoming edges and zero out going edges