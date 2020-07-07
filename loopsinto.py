even_number = [2,4,6,8] #loop and print list 
for num in even_number:
	print num
	
numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
	#check if number is even
	if num %2 == 0:
		print num
		
counter = 1
while counter < 10:
	print counter
	counter += 1
	
for x in range(10):
	print(x)
	if x==5:
		break

import string
for letter in string.ascii_lowercase:
	if letter == "a":
		continue	#print all letters except 'a'
	print letter