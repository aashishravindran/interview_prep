# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        ans=float('inf')
        cs=0
        left=0
        for i in range(len(nums)):
            cs+=nums[i]
            while cs>=s:
                
                ans=min(ans,(i-left)+1)
                cs-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0
                
                