# //https://leetcode.com/problems/course-schedule/submissions/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        import collections
        graph=collections.defaultdict(list)
       
        for u,v in prerequisites:
            graph[u].append(v)
        
        visited=["White"]*numCourses
        print(graph)
        def hasCycle(node):
            
            if visited[node]=="Gray":
                return True
            visited[node]="Gray"
            for adjacents in graph[node]:
                if visited[adjacents]!="Black":
                    if hasCycle(adjacents):
                        return True
            
            visited[node]="Black"
            return False
        
        
        for i in range(numCourses):
            if visited[i]=="White" and hasCycle(i):
                return False
        return True