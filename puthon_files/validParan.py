# https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        master={')':'(',']':'[','}':'{'}
        
        for par in s:
            if par in master:
                if not stack:
                    return False 
                
                if stack and master[par]!=stack.pop():
                    return False 
                
            else:
                stack.append(par)
        
        return not stack 