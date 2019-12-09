# sliding-window-maximum
# https://leetcode.com/problems/sliding-window-maximum/
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return None
        lent=len(nums)
        maxval=[]
        
        for start in range((lent-k)+1):
            max_ele=max(nums[start:start+k])
            maxval.append(max_ele)
            
            
        return maxval