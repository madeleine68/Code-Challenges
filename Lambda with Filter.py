#Rewrite this code to be more concise by replacing the is_short function with a lambda 
#expression defined within the call to filter().

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

is_short=lambda name: len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)