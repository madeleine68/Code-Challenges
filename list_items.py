def list_item (list, value):
	"""a function to find all indices of a given value in a list."""
	indices =[]
	# Iterate through list to 
	for i in range(len(liste)):
		if liste[i] == value:
			 indices.append([i])

		# if list contain other list 	 
		elif type(liste[i]) is list:
			# using recursive method to find index in sublist
			for index in list_item(liste[i],value):
				# catenate the index of the list to the front of index value
				indices.append ([i]+index)
	return indices		

