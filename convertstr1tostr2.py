class convert:
	def xtoy(self,x,y):
		lst1=[]
		lst2=[]
		c=0
		for i in x:
			lst1.append(i)
		for i in y:
			lst2.append(i)
		if len(lst1)<len(lst2):
			for i in range(len(lst1),len(lst2)):
				lst1.append('0')
		else:
			for i in range(len(lst2),len(lst1)):
				lst2.append('0')
		for i in range(len(lst1)):
			if lst1[i]!=lst2[i]:
				c+=1
		print(c)

x,y=input().split()
call=convert()
call.xtoy(x,y)
				
		
