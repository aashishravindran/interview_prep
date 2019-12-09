
mem_full and en_acc done 
counter implementation for reset addr 
	//adding counters to the control logic to icrement f and x separately
	//reset when both are met c_x=n-1 and c_f=M-1

conv logic:
	if en_acc:
		set both addr_x and add_f to 0 




for n = 0 to L-1:
	y[n] = 0
for k = 0 to M-1:
	y[n] += x[n+k]*f[k]

x=3
f=5

N=size(x)
M=size(f)

L=N-M+1


