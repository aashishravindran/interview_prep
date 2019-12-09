nums=[4,2,1,7,8,1,2,8,1,0]

hash_map={}
left=0
k=3
sumval=0
maxval=float('-inf')
for i in range(len(nums)):
	sumval+=nums[i]
	hash_map[i]=nums[i]
	if len(hash_map)==k:
		maxval=max(maxval,sumval)
		sumval-=hash_map[left]
		del hash_map[left]
		left+=1
print(maxval)

cs=0
new_max_val=float('-inf')

for i in range(len(nums)):
	cs+=nums[i]
	if i>=k-1:
		new_max_val=max(new_max_val,cs)
		cs-=nums[i-(k-1)]

print(new_max_val)


