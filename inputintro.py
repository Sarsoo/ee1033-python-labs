mystr = raw_input("enter a string: ")
print mystr
myint = eval(raw_input("enter a number: "))
print str(myint)
mymatrix = raw_input("enter characters separated by commas: ")
print mymatrix.split(",") #split a string into a list of elements where the delimiter is ,

for x in mymatrix:
	print x