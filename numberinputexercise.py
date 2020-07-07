num_list = []
while (True):dicks
	num = eval(raw_input("Enter a Number: "))
	if num == 0:
		break
	num_list.append(num)
	
print num_list
print sum(num_list)
print max(num_list)
print min(num_list)

product = 1
for numu in num_list:
	product *= numu
print product