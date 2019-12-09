
# https://leetcode.com/problems/word-search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row=len(board)
        col=len(board[0])
        
        
        def dfs(board,i,j,count,word):
            if count==len(word):
                return True
            if (i<0 or i>=row) or (j<0 or j>=col) or board[i][j]!=word[count]:
                return False
            
            temp=board[i][j]
            board[i][j]=' '
            value= dfs(board,i+1,j,count+1,word) or dfs(board,i-1,j,count+1,word) or dfs(board,i,j+1,count+1,word) or dfs(board,i,j-1,count+1,word)
            board[i][j]=temp
            return value
            
        
    
        for i in range(row):
            for j in range(col):
                
                if board[i][j]==word[0] and dfs(board,i,j,0,word):
                    return True
        return False
    
    
    