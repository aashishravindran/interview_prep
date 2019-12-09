def conv_function(x,f):

	N=len(x)
	M=len(f)
	L=(N-M)+1
	y=[None]*L 
	for n in range(0,L):
		y[n]=0
		for k in range(M):
				y[n]+=(x[n+k]*f[k])

	return y


result=[]
x_count=0
y_count=0
x=[10,-20,30,-40,50,60,70,80,-90, 100, -110, 120, -50, 40, 30, -20]
f=[10,20,-30,40, -50, -60, 70, 80]

while x_count<len(x) and y_count<len(f):

	temp_x=x[x_count:x_count+8]
	temp_f=f[y_count:y_count+4]
	ret=conv_function(temp_x,temp_f)	

	for r in ret:
		print(r)
		result.append(r)

	x_count+=8
	y_count+=4

print(result)

# for n = 0 to L-1:
# y[n] = 0
# for k = 0 to M-1:
# y[n] += x[n+k]*f[k]