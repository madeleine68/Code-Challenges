N=int(input())
X=list(map(int, input().split()))
W=list(map(int, input().split()))

total=0
for j in W:
    total+=j
m=0    
for i in range(N):
     m+= X[i]*W[i]
print(round(m/total,1))       
