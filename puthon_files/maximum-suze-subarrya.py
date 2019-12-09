
#https://leetcode.com/problems/maximum-size-subarray-sum-equals-k

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        sumval=0
        
        hashm={0:-1}
        for num in range(0,len(nums)):
            sumval+=nums[num]
            
            if (sumval-k) in hashm:
                
                ans=max(ans,num-hashm[sumval-k])
            if sumval not in hashm: # avoiding duplicates of prv encountered sums 
                hashm[sumval]=num
                
            
        return ans