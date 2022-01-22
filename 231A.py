n=int(input())
c=0
for i in range(n):
    n=list(map(int,input().split()))
    if (n[0]+n[1]+n[2])>=2:
        c=c+1
print(c)        
        
