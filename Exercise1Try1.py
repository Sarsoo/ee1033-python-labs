numbers = [6,2,9,0,2,5,3]				#list of input numbers
print numbers							#test
#sorted = [numbers[0]]
sorted = []								#list of sorted numbers
#print sorted							#test
counter = 1								#counter to be used as reference for input numbers list
sorted_counter = counter-1				#coutner to be used as reference for positioning in sorted list
#print sorted_counter					#test
#print len(numbers)						#test
#while counter <= len(numbers):
#	if numbers[counter] < sorted[sorted_counter]:
#		sorted.insert(sorted_counter, numbers[counter])
#		counter += 1
#		print sorted
#		print counter
#	else:
#		counter += 1

for x in numbers:
	print x
	if counter == 1:
		sorted.append(x)
		counter += 1
	else:
		for y in sorted:
			if x < y:
				print "yes"
				break
#	if numbers[x] < sorted[sorted_counter]:
#		sorted.insert(sorted_counter, numbers[counter])
#		counter += 1
#		print sorted
#		print counter
#	else:
#		counter += 1