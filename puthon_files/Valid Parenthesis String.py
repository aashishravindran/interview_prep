# Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        for i in s:
            if i=='(' or i=="*":
                left+=1
            else:
                left-=1
            
            if left<0:
                return False
        if left ==0:
            return True
        
        right=0
        
        for j in reversed(s):
            if j==')' or j=="*":
                right+=1
            else:
                right-=1
            
            if right < 0:
                return False
            
            
        return True 
        
        
        
        
        
        