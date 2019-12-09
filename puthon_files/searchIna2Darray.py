# https://leetcode.com/problems/search-a-2d-matrix/
# 74. Search a 2D Matrix


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
        
        n=len(matrix[0])
        
      
        left=0
        right=m*n-1
        while left<=right:
            pivot=(left+right)/2
            pivot_ele=matrix[pivot//n][pivot%n]
            if pivot_ele==target:
                return True
            if pivot_ele<target:
                left=pivot+1
            else:
                right=pivot-1
        
        return False 
