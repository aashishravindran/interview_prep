# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        s=S
        stack=[]
        left=0
        for i in s:
            if stack and i==')' and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
        
        return len(stack)