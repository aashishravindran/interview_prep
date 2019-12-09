# https://leetcode.com/problems/is-graph-bipartite/
# 785. Is Graph Bipartite?
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        import collections 
        
        made= collections.defaultdict(list)
        
        for u in range(len(graph)):
            made[u]=graph[u]
            
        queue=collections.deque()
        color_matrix=["UNC"]*len(graph)
        seen=set()
        
        for i in range(len(graph)):
            if i not in seen:
                queue.append(i)
                seen.add(i)
                color_matrix[i]="White"
                
                while queue:
                    node=queue.popleft()
                    for adjacents in made[node]:
                        adjacentColor=color_matrix[adjacents]
                        if adjacentColor=="UNC":
                            color_matrix[adjacents]="White" if color_matrix[node]=="Black" else "Black"
                        elif adjacentColor == color_matrix[node]:
                            return False
                        if adjacents not in seen:
                            queue.append(adjacents)
                            seen.add(adjacents)
                            
       # print(color_matrix)                   
        return True
                    
                        
                
        
        
       
       