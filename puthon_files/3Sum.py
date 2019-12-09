# https://leetcode.com/problems/3sum/
# 3 Sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output=set()
        
        for i in range(len(nums)-2):
            first=i
            left=first+1
            right=len(nums)-1
            
            while left<right:
                sumval=nums[first]+nums[left]+nums[right]
                
                if sumval==0:
                    output.add((nums[first],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif sumval<0:
                    left+=1
                else:
                    right-=1
        return output