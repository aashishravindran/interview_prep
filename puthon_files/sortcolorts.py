# https://leetcode.com/problems/sort-colors
# 75. Sort Colors
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero=0
        curr_wp=0
        last=len(nums)-1
        while curr_wp<=last:
            if nums[curr_wp]==0:
                nums[curr_wp],nums[zero]=nums[zero],nums[curr_wp]
                zero+=1
                curr_wp+=1
            elif nums[curr_wp]==2:
                nums[curr_wp],nums[last]=nums[last],nums[curr_wp]
                last-=1
            else:
                curr_wp+=1
            