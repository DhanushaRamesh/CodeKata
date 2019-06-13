lst=[]
class write:
	def oddeveplacenot(self,n,arr):
		for i in range(n):
			if i%2==0:
				if arr[i]%2!=0:
					lst.append(arr[i])
			else:
				if arr[i]%2==0:
					lst.append(arr[i])
		for i in range(len(lst)):
			if i==(len(lst))-1:
				print(lst[i])
			else:
				print(lst[i],end=" ")
n=int(input())
arr=list(map(int,input().split()))
c=write()
c.oddeveplacenot(n,arr)
