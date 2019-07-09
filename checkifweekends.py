class check:
	def weekends(self,day):
		lst=['Saturday',"Sunday"]
		if day in lst:
			print('yes')
		else:
			print('no')
day=input()
call=check()
call.weekends(day)
