a=5
b=2

try:
	print("resource  is opened")
	print(a/b)
	k=int(input("enter  the number"))
	print(k)
#ZeroDivisionError
except ZeroDivisionError as a:
	print("Hey ,you cannot divide a divisor by zero",a)
#ValueError
except ValueError as a:
	print(" Invalid Input -> ",a)
#Except block will execute only if there is a error
except Exception as a:
	print("something went wrong")
finally:
	print("done")
#finally block will execute if we get error as well as if we dont get error
