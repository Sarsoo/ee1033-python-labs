unsorted_array = [6,2,9,0,2,5,3]	#array of values given by exercise
sorted_array = []	#empty array that will be populated by sorted values

while unsorted_array:		#open while loop, active while the unsorted array still has values in it
	minimum_value = unsorted_array[0]	#takes first value in array and sets it as "minimum value"
	for x in unsorted_array:			
		if x < minimum_value:			#for loops check "minimum value" against each value in array 
			minimum_value = x			#and sets it as new "minimum value" if a value is found that is smaller
	sorted_array.append(minimum_value)	#adds smallest value from unsorted array to the first value of the sorted array
	print minimum_value					#prints smallest value
	unsorted_array.remove(minimum_value)#removes smallest value from unsorted array so it can not be picked and added again	