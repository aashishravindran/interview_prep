## Code for topoligical sort
#visist every 
from collections import defaultdict 

topo_stack=[]

def make_graph(g):
	print("Here")
	graph=defaultdict(list)
	for u,v in g:
		graph[u].append(v)

	return graph

def dfs_iterative(start,graph):
   visited=set()
   stack=[]
   stack.append(start)
   
   ret=[]
   while  stack:
        node=stack.pop()
        if node not in visited :
            visited.add(node)
            ret.append(node)
        for i in range(len(graph[node])-1,-1,-1):
            if graph[node][i] not in visited:
                stack.append(graph[node][i])
        
   return ret



def dfs_recursive(node,graph,seen):
		seen.add(node)
		print(node)
		for i in graph[node]:
			if i not in seen:
				dfs_recursive(i,graph,seen)


def toposort(vertex,new_adj_list,visited):
	visited.add(vertex)
	for val in new_adj_list[vertex]:
		if  val not in visited:
			toposort(val,new_adj_list,visited)
	topo_stack.append(vertex)

def topological_sort_driver(graph):
	new_adj_list=make_graph(graph)
	visited=set()
	
	for key,value in new_adj_list.items():
		if key not in visited:
			toposort(key,new_adj_list,visited)
		
	return topo_stack
		
def call_dfs(vertex,adj_list,visited):

	if visited[vertex]==-1:
		return True
	if visited[vertex]==1:
		return False
	visited[vertex]=-1
	for i in adj_list[vertex]:
		 if call_dfs(i,adj_list,visited):
		 	return True
	visited[vertex]=1
	return False 

def detect_cycle_directed_graph(graph,adj_list):
	visited=[0]*len(graph)
	for i in range(len(graph)):
		if call_dfs(i,adj_list,visited):
			return True
	return False 


graph=[['A','B'],['A','F'],['B','H'],['D','C'],['D','I'],['D','E'],['G','B'],['I','C'],['J','E']]

graph_made=make_graph(graph)
visited=[False]*len(graph)
# print(detect_cycle_directed_graph(graph,graph_made))
print(graph_made)
print(topological_sort_driver(graph))
# topological_sort_dfs(5,visited,graph_made)

			
t=[[0,1],[0,2],[0,3],[2,4],[3,5]]

t=make_graph(t)
# print(t)
print(dfs_iterative(0,t))
print(dfs_recursive(0,t,set()))
