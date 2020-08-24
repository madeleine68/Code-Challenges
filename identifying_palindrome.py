def isPalindrome(str):
	"""check if the given string is palindrom """
	# remove any space from both side of the string,
	# and convert to lower case letter
	str = str.strip()
	str = str.lower()

	# Run loop from starting to length/2 and check the first
	# character to the last character and so on
	a = int(len(str)/2)
	for i in range(0, a):
		if str[i] != str[len(str)-i-1]:
			return False
	return True


		