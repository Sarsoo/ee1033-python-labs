rows = eval(raw_input("Enter Row Number: "))	#user defines number of columns
columns = eval(raw_input("Enter Column Number: "))	#user defines number of columns

matrix = []	#define empty matrix

for i in range(0, rows):		#populates matrix with user elements
	newrow = [] 
	for j in range(0, columns):	#defines a row of elements added by user and appends it to matrix
		num = int(raw_input("Enter Matrix Element: "))
		newrow.append(num)
	matrix.append(newrow)
	
for i in matrix:	#print first matrix
	print i
	
transposed_matrix = []	#defines new matrix which will become transpose of previous matrix

for i in range(0, columns):	#same function as before to populate new matrix, defining number of rows as 
	newrow = [] 			#previous matrix had columns and vise versa
	for j in range(0, rows):
		num = matrix[j][i]	#takes each element from previous matrix rather than user input as before
		newrow.append(num)
	transposed_matrix.append(newrow)

for i in transposed_matrix:
	print i					#print transpose matrix