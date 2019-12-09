# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/submissions/
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """       
        import collections
        graph=collections.defaultdict(list)
        visited=["White"]*numCourses
        topsort=[]
        for u,v in prerequisites:
            graph[u].append(v)
            
        def hasCycle(node):
            if visited[node]=="Gray":
                return True
            visited[node]="Gray"
            for adjacents in graph[node]:
                if visited[adjacents]!="Black":
                    if hasCycle(adjacents):
                        return True
            visited[node]="Black"
            # print(node)
            topsort.append(node)
            return False
        
        for i in range(numCourses):
            if visited[i]=="White" and hasCycle(i):
                return []
        
        return topsort