#Write a function named readable_timedelta. The function should take one argument, an integer days,
# and return a string that says how many weeks and days that is

def readable_timedelta(day):
	weeks = day // 7
	days = day % 7 

	return "{} week(s) and {} day(s).".format(weeks,days)

	# test your function
print(readable_timedelta(10))