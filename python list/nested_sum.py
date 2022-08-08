a=[[1,3,1],[1,5,1],[4,2,1]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        if i>0:
            sum=sum+a[i][-1]
        j=j+1
    i=i+1
print(sum)
        
        
        

    