day_1 = eval(raw_input("Enter Day 1: "))
month_1 = eval(raw_input("Enter Month 1: "))
year_1 = eval(raw_input("Enter Year 1: "))
day_2 = eval(raw_input("Enter Day 2: "))
month_2 = eval(raw_input("Enter Month 2: "))
year_2 = eval(raw_input("Enter Year 2: "))

month_length = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_1_math = month_1
day_sum = 0
while month_1_math != 0:
	day_sum += month_length[month_1_math]
	month_1_math -= 1

month_2_math = 11 - month_2
day_sum_2 = 0
while month_2_math != 0:
	day_sum_2 += month_length[month_2_math]
	month_2_math -= 1

day_2_difference = month_length[month_2] - day_2

year_dif = ((year_1 - year_2 - 1)*365)

if year_dif < 0:
	year_dif = 0
	
total = year_dif + day_sum + day_1 + day_sum_2 + day_2_difference
print total
#delta_day = day_2 - day_1
#delta_month = month_2 - month_1
#delta_year = year_2 - year_1 - 1

#
#if day_2 < day_1:
#	delta_month -= 1
#
#if month_2 < month_2:
#	delta_year -= 1

