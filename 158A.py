n,k=map(int,input().split())
m=list(map(int,input().split()))
c=0
p=m[k-1]
for i in range(n):
    if (m[i]>=p)and(m[i]!=0):
        c=c+1
print(c)        
