N=int(input())
X=list(map(int,input().split()))

#average
total=0
for i in X:
    total+=i
avg=total/N    

#calculate the dominator
top=0
for j in range (N):
    top+=(X[j]-avg)**2


sigma=(top/N)**(0.5)
print(round(sigma,1))