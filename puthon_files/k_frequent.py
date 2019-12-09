arr=[1,1,1,2,2,3,3,3,3]
temp_arr={}
k=2
for i in arr:
	if i in temp_arr:
		temp_arr[i]=temp_arr[i]+1
	else:
		temp_arr[i]=1
print(temp_arr)
output=[]
while k>0:
	
	max_key=max(temp_arr.items(), key=lambda x : x[1])
	output.append(max_key[0])
	del temp_arr[max_key[0]]
	k-=1
print(output)




