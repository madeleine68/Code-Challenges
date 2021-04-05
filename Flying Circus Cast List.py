#Write a function called create_cast_list that takes a filename as input and returns a list of actors' names.
def create_cast_list (filename):
	cast_list=[]
	with open(filename) as f:
		for line in f:
			cast_list.append(line.split(",")[0])

	return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
