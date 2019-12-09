
# https://leetcode.com/problems/sliding-window-maximum/submissions/
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        maxval=max(nums[:k])
        res=[]
        res.append(maxval)
        for i in range(k,len(nums)):
            if nums[i]>maxval:
                res.append(nums[i])
                maxval=nums[i]
            elif maxval!=nums[i-k]:
                res.append(maxval)
            else:
                maxval=max(nums[i-k+1:i+1])
                res.append(maxval)
        return res