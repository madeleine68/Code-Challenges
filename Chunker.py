#Implement a generator function, chunker, that takes in an iterable and yields a chunk
# of a specified size at a time.

def chunker(iterable, size):
    # Implement function 
    for i in range (0, len(iterable), size):
    	yield iterable[i:i+size]


for chunk in chunker(range(25), 4):
    print(list(chunk))