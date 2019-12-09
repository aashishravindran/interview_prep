#QUick Sort

# Algorithm : 
# 1) pick a pivot element and partition the array such taht alll elements to the left of the 
# pivot are less than all elements to the right of the pivot 

# 2) call quicksort on the segemnt  start to p-1 
# 3) call quick sort on the elemnt p+1 to end 
# 4) Base cases: end the recursion if start>=end

def QuickSort(arr,start,end):

	if start<end:
		pindex=partition(arr,start,end)
		QuickSort(arr,start,pindex-1)
		QuickSort(arr,pindex+1,end)


def partition(arr,start,end):
	pivot=arr[end]
	part_index=start
	for i in range(start,end):
		if arr[i]<=pivot:
			arr[i],arr[part_index]=arr[part_index],arr[i]
			part_index+=1

	arr[part_index],arr[end]=arr[end],arr[part_index]

	return part_index


# arr_1=[4,322,9,11]
# QuickSort(arr_1,0,len(arr_1)-1)
# print(arr_1)

# Merge Sort

def MergeSort(nums):
	if(len(nums))<=1:
		return nums

	pivot_ele = int(len(nums) / 2)
	##get left half
	left=MergeSort(nums[0:pivot_ele])
	right=MergeSort(nums[pivot_ele:])
	return merge(left,right)


def merge(left_list,right_list):
	left,right=0,0
	res=[]
	while left<len(left_list) and right<len(right_list):
		if left_list[left] <right_list[right]:
			res.append(left_list[left])
			left+=1
		else:
			res.append(right_list[right])
			right+=1
	res.extend(left_list[left:])
	res.extend(right_list[right:])
	return res

arr_1=[4,4,9,11]
new=MergeSort(arr_1)
print(new)


# final=ListNode(-1)
#         curr=final
        
#         while l1 and l2:
#             print(curr.val)
#             if l1.val < l2.val:
#                 curr.next=l1
#                 l1=l1.next
#             else:
#                 curr.next=l2
#                 l2=l2.next
#             curr=curr.next
        
#         ##
#         curr.next = l1 if l1 is not None else l2

#         return final.next


 # def reverse_helper(self,head,count):
 #        prev=None
 #        curr=head
 #        while count>0:
 #            nextval=curr.next
 #            curr.next=prev
 #            prev=curr
 #            curr=nextval
 #            count-=1
 #        return (curr,prev)
    
    
 #    def reverseKGroup(self, head, k):
 #        """
 #        :type head: ListNode
 #        :type k: int
 #        :rtype: ListNode
 #        """
 #        count=0
 #        temp=head
 #        while temp is not None and count<k:
 #            temp=temp.next
 #            count+=1
 #        if count<k: 
 #            return head
 #        new_head,prev=self.reverse_helper(head,count)
 #        head.next = self.reverseKGroup(new_head, k)
 #        return prev
        
 #        #