def plus_one(arr):

	end=len(arr)-1
	if arr[end]<9:
		arr[end]+=1
		return arr

	j=end;

	while j>=0:
		if arr[j]==9:
			arr[j]=0
		else:
			arr[j]+=1
			return arr
		j-=1
	arr[0]=1
	return arr
print(plus_one([1,2,3,9,9]))  