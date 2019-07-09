lstit=[]
class longest:
	def prefix(self,str1,str2):
		n=0
		lstit=[]
		if len(str1)<len(str2):
			n=len(str1)
		else:
			n=len(str2)
		for i in range(n):
			if str1[i]==str2[i]:
				lstit.append(str1[i])
		return(lstit)
		
		
n=int(input())
lst=[]
for i in range(n):
	stri=input()
	lst.append(stri)
	
call=longest()
for i in range(0,n):
	for j in range(i):
			longetprefix=call.prefix(lst[i],lst[j])
for i in range(len(longetprefix)):
	if i == len(longetprefix)-1:
		print(longetprefix[i])
	else:
		print(longetprefix[i],end="")

