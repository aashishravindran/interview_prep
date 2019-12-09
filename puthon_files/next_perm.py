def reverse_list(nums,left):
    right=len(nums)-1
    while left<right:
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1
    return nums



def nextPermutation(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        right=len(nums)-2        
        while right>=0 and nums[right+1]<+nums[right]:
            right-=1
        
        ele=nums[right]
        rever_idx=right
        # print(ele)
        if rever_idx>=0: 
            new_right=len(nums)-1
            while new_right>=0 and nums[new_right]>=ele:
                new_right-=1
        
        
            print(new_right)
            nums[rever_idx],nums[new_right]=nums[new_right],nums[rever_idx]

        return reverse_list(nums,rever_idx+1)

arr=[1,1,5]
print(nextPermutation(arr))