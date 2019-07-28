def fibo(n):
	n1,n2=0,1
	if n==1:
		print(n1)
	elif n==2:
		print(n1," ",n2)
	else:
		print(n1,n2,end=" ")
		for i in range(3,n+1):
			temp=n1
			n1=n2
			n2=temp+n2
			print(n2,end=" ")
		
		
n=int(input("how many fibonacci numbers you need: "))
fibo(n)
		
	
	
	
