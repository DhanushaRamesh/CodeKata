lst=[]
lst1=[]
class formsmall:
	def no(self,n,k):
		for i in n:
			lst1.append(i)
		for i in range(k,len(lst1)):
			lst.append(lst1[i])
		#lst.sort()
		for i in range(len(lst)):
			if i==len(lst)-1:
				print(lst[i])
			else:
				print(lst[i],end="")
n,k=map(str,input().split())
call=formsmall()
call.no(n,int(k))
