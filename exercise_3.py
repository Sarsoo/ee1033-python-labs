print "Function takes Date 1 and subtracts Date 2, enter string of integers separated by spaces"

date_1 = raw_input("Enter date 1 in format dd mm yyyy: ")	#takes dates as string of integers
date_2 = raw_input("Enter date 2 in format dd mm yyyy: ")

date_1 = [int(i) for i in date_1.split() if i.isdigit()]	#creates array of integers extracted from string input
date_2 = [int(j) for j in date_2.split() if j.isdigit()]

month_length = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
#month_length is array of months denoted by cumulative days up to month before month entered hence 0,0 at the start
#ie entering 1 as january will return 0 as no complete months have passed 
#entering 3 for march will return 59 representing january's and february's complete days

def date_to_days(day, month, year):	#function defined to take date and turn it into days
	year *= 365	#takes total years inputed and multiplies it by 365
	month = month_length[month] 	#returns days in month from array previously explained
	return day + month + year		#returns total days as sum of previous calculations
	
date_1_days = date_to_days(date_1[0], date_1[1], date_1[2])	#calls function for first date
date_2_days = date_to_days(date_2[0], date_2[1], date_2[2])	#calls function for second date

#print date_1_days	#prints everything
#print date_2_days
print abs(date_1_days-date_2_days) #takes absolute value so days is always positive