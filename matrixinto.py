mymatrix = [[1,2,3], [4,5,6], [7,8,9]]
#to iterate through rows
for i in range(len(mymatrix)):
	print i
	print(mymatrix[i])

#ask user for the number of columns and rows, then creates the matrix
rows = int(raw_input("enter number of rows: "))
columns = int(raw_input("enter number of columns: "))
#create matrix
mymatrix = []
for i in range(0, rows):
	myrow = [] #row has to be initialized ever iteration
	for j in range(0, columns):
		num = int(raw_input("enter a number: "))
		myrow.append(num)
	mymatrix.append(myrow)
	
for i in range(len(mymatrix)):
	print i
	print(mymatrix[i])