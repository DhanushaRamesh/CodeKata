lst=[]
class find:
	def repeat(self,n,arr):
		for i in range(n):
			for j in range(i+1,n):
				if arr[i]==arr[j]:
					lst.append(arr[i])
		if len(lst)==0:
			print("unique")
		else:
			print(lst[2])
n=int(input())
arr=list(map(int,input().split()))
c=find()
c.repeat(n,arr)
