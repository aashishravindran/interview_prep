# https://leetcode.com/problems/letter-combinations-of-a-phone-number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        output=[]
        
        
        def generate_comb(letter,index):
            if len(letter)==len(digits):
                output.append(letter)
                return 
            else:
                for i in phone[digits[index]]:
                    generate_comb(letter+i,index+1)
        
        generate_comb("",0)
        return output