unsorted_array = [6,2,9,0,2,5,3]
sorted_array = []

while unsorted_array:
	minimum_value = unsorted_array[0]
	for x in unsorted_array:
		if x < minimum_value:
			minimum_value = x
	sorted_array.append(minimum_value)
	unsorted_array.remove(minimum_value)
	print sorted_array[len(sorted_array)-1]
#print sorted_array