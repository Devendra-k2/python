
list=[1,2,3,2,1]
le=len(list)
l=int(len(list)/2)
for i in range(l) :
	if(list[i]==list[le-1]):
		print(le-1)
		f=0
	else:
		f=1
if f==0 :
	print("palindrome")
else :
	print("no")