import collections
collections.defaultdict(list)


def make_graph(g):
	print("Here")
	graph=collections.defaultdict(list)
	for u,v in g:
		graph[u].append(v)
		graph[v].append(u)
	return graph



inputval=[['A','B'],['A','F'],['B','H'],['D','C'],['D','I'],['D','E'],['G','B'],['I','C'],['J','E'],['F','C'],['G','E'],['G','D']]


graph=make_graph(inputval)

queue=collections.deque()

seen=set()
out=[]
print(graph)

def BreadthFirstSearch(graph):
		seen.add(inputval[0][0])

		queue.append(inputval[0][0])
		

		while queue:
			ele=queue.popleft()
			
			out.append(ele)
			for adjagents in graph[ele]:
				print(adjagents)
				if adjagents not in seen:
					seen.add(adjagents)
					queue.append(adjagents)
					
		return None




BreadthFirstSearch(graph)
print(out)
