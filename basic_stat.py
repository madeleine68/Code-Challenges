#average
N = int(input())
numbers = list(map(int, input().split()))
total=0
for i in numbers:
    total+=i
avg=total/N
print(avg)

#median
numbers.sort()
if N % 2 != 0 :
    med = numbers[((N-1)//2)+1]
else:
    med = (numbers[(N-1)//2]+numbers[((N-1)//2)+1])/2
print(med)    
#Mode
mode=max(numbers, key=numbers.count)
print(mode) 
