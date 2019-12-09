
# https://leetcode.com/problems/keys-and-rooms/
## 841 Keys and Rooms
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        import collections 
        graph=collections.defaultdict(list)
        
        for i in range(len(rooms)):
            graph[i]=rooms[i]
        
        visited=set()
        
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for adjacents in graph[node]:
                    dfs(adjacents)
            
        dfs(0)
     
        if len(visited) == len(rooms):
            return True
        else:
            return False