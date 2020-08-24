def sort_word (input):
	""" function to sorts the words in a string alphabetically"""
	# string of words separated by spaces, so by using split function it
	# breaks apart the input string at each of spaces and gives a list of words
	words = input.split()
	for i in words:
	# sort function witll priotrize words beginning with capital letters
	# ahead of words with lowercase letter
		words.sort(key=lambda L: (L.lower(), L))
	# assemble the list of words back

	return (' '.join(words))
