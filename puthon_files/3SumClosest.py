# https://leetcode.com/problems/3sum-closest
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        closest=2**31 -1
        
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                curr_sum=nums[i]+nums[j]+nums[k]
                if curr_sum==target:
                    return curr_sum
                if abs(curr_sum-target)<abs(closest-target):
                    closest=curr_sum
                if curr_sum<target:
                    j=j+1
                else:
                    k=k-1
        return closest
            
         
                    k=k-1
        return closest
            
         