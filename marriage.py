class TooYoungException(Exception): 
	def __init__(self,arg): 
		self.msg=arg 

class TooOldException(Exception): 
	def __init__(self,arg): 
		self.msg=arg 

age=int(input("Enter Age:")) 

if age>60: 
	raise TooOldException("Your age already crossed marriage age...no chance of getting marriage") 

elif age<18: 
	raise TooYoungException("Please wait for few more years") 

else: 
	print("You will get match details soon by email!!!")