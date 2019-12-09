# https://leetcode.com/problems/maximum-subarray/
# Greedy 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=nums[0]
        max_global=nums[0]
        
        for i in range(1,len(nums)):
            
            curr=max(nums[i],curr+nums[i]) ## at every point check if i need to include that elemnt in the sum or 
            ## exclude in the sub 
            max_global=max(curr,max_global)
        
        return max_global 