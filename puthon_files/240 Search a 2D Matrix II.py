# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])-1
        
        row=0
        col=n
        while col>=0 and row<m:
            if target==matrix[row][col]:
                return True
            if matrix[row][col]>target:
                col-=1
            if matrix[row][col]<target:
                row+=1
        
        return False 