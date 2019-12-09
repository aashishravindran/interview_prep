"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# https://leetcode.com/problems/clone-graph
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        import collections
        queue=collections.deque([node])
        hash_map={}
        
        hash_map[node]=Node(node.val,[])
        
        while queue:
            copy_node=queue.popleft()
       
            
            for adjacents in copy_node.neighbors:
                if adjacents not in hash_map:
                    
                    hash_map[adjacents]=Node(adjacents.val,[])
                    queue.append(adjacents)
                hash_map[copy_node].neighbors.append(hash_map[adjacents])
           
        
        return hash_map[node]
        
        