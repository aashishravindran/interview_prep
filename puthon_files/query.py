
def get_ways(a,b,target,count,i,j):

	if (target-(a[i]+b[j]))==0:
		
		count[0]+=1
	elif (target-(a[i]+b[j]))<0:
		return None
	else:
		get_ways(a,b,target,count,i,j+1)
		get_ways(a,b,target,count,i+1,j)
	return count

	

a=[1,2,3]
b=[3,4]
query=[[1,5],[0,1,5],[1,5]]
a.sort()
b.sort()

res=[]
total_ways=0
for q in query:
	if len(q)==2 and q[0]==1:
		print(q[1])
		t=get_ways(a,b,q[1],[0],0,0)
		res.append(t[0])
	elif len(q) == 3 and q[1]<len(b):
		b[q[1]]=q[2]
		a.sort()
		b.sort()

print(res)