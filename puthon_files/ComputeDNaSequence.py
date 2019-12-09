# https://leetcode.com/problems/repeated-dna-sequences
#187. Repeated DNA Sequences
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L=10
        n=len(s)
        output,seen=set(),set()
        for start in range(n-L+1):
            tmp=s[start:start+L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
            
        return output