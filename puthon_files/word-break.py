# https://leetcode.com/problems/word-break/
# 139. Word Break
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set=set(wordDict)
        memo={}
        
        def dfs(curr_string,word_set):
            if curr_string=='':
                return True
            if curr_string  in memo:
                return memo[curr_string]
            
            for i in range(1,len(curr_string)+1):
                if curr_string[0:i] in word_set and dfs(curr_string[i:],word_set):
                        memo[curr_string[i:]]=True
                        return True
                    
                memo[curr_string]=False
            return False
        
        
        return dfs(s,word_set)
        
