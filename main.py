year = int(input("Enter a year: "))

'''
Leap year usually occurs every 4 years 
(divisible by 4) BUT, if leap year is 
on a century (divisible by 100), then 
that century must be divisible by 400 
to be considered a leap year.
'''

if (year % 100 == 0):
	if (year % 400 == 0):
		print (str(year) + " is a leap year.")
	else:
		print (str(year) + " is not a leap year.")

elif (year % 4 == 0):
	print (str(year) + " is a leap year.")

else:
	print (str(year) + " is not a leap year.")
