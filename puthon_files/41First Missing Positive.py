# https://leetcode.com/problems/first-missing-positive/

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}
        for i in range(len(nums)):
            if nums[i]>0:
                hash_map[nums[i]]=i
        
        j=1
        if 1 not in hash_map:
            return 1
        
        while True:
            if j not in hash_map:
                return j 
            j+=1