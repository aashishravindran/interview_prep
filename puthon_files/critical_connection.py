class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        ## The gaol is to find the number of bridges in an undirected graph 
        ## A bridge is definded as an edge which when removed can increase the number of 
        ## critical components 
        ## By "disconnecting" the graph we make certain vertexes inaccesible 
        
        ##### A low link value is the smallest node id which can be visited from that node 
                    ## ex [0,1] [1,0][0,2][2,0]  low[0]-[0] low[1]-0
        import collections
        ##standard boilerplate to make graph 
        graph =collections.defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        ##undie graph to make key value mapping of both the vertexes
        visited=set() ## goign to keep track of the nodes we visist 
        res=[]
        parent=[-1]*n ## numbet of nodes 
        self.clock=0 ##  we use this to assign a unique id to each node we visit 
        low_time=[float('inf')]*n ## low link time 
        visited_time=[float('inf')]*n # time we visited a node
        ## while doing dfs if visisted_time[node]<low_link time of the adjacent 
            ## then the paren node and its adjacents are bridges 
        
        
        def dfs(node):
            low_time[node]=self.clock
            visited_time[node]=self.clock
            self.clock+=1
            visited.add(node)
            for adjacents in graph[node]:
                if adjacents not in visited:
                    parent[adjacents]=node
                    dfs(adjacents)
                    ## on the call back update the low time as follws 
                    low_time[node]=min(low_time[node],low_time[adjacents])
                    ## we do this to update the low_link value of that node 
                    
                    
                    if visited_time[node]<low_time[adjacents]:
                        
                        ## if the visited_time or id if the node is less that the low_link time of the node then those vertexes are edjes
                        
                        res.append([node,adjacents])
                        
        
                elif adjacents!=parent[node]:
                        ## we also update the lowtime of the parent, whne we try to visist a prevously visisted node, that has a chance of 
                        ## having a lesser low link value
                        low_time[node]=min(low_time[node],visited_time[adjacents])
                        
        for i in range(n):
            if i not in visited:
                dfs(i)
                #initiate the dfs 
        
        return res
        