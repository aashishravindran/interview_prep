"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) 
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

##bottom up approach
def longestCommonSubsequence(text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
                       
        dp_arr=[[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        maxval=0
        
        for i in range(1,len(dp_arr)):
            for j in range(1,len(dp_arr[0])):
                if text1[i-1] == text2[j-1]:
                    dp_arr[i][j]=dp_arr[i-1][j-1]+1
                else:
                    dp_arr[i][j]=max(dp_arr[i-1][j],dp_arr[i][j-1])
                    
        return dp_arr[len(text1)][len(text2)]

## recursive algorithmp 

def lcs_recursive(text1,text2):
    if not text1 or not text2:
        return 0
        ## Base case .. comparing " " with and " " will always return zeros
    # check then if the last characters are equal
    if text1[len(text1)-1] == text2[len(text2)-1]:
        # since both are equal remove the last character and call lcs again
        return 1 + lcs_recursive(text1[0:len(text1)-1],text2[0:len(text2)-1])
    else:
        # since the chars are not equal, lcs becomes the max of lcs withouth either chars 
        # for examps "aaz" and "aa"
        return max(lcs_recursive(text1,text2[0:len(text2)-1]),lcs_recursive(text1[0:len(text1)-1],text2))



text1="bsbininm"
text2="jmjkbkjkv"
a=lcs_recursive(text1,text2)
print(a)


